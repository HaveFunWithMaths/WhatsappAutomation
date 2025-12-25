"""
WhatsApp Business API Message Sender
=====================================
This script reads contacts from an Excel file and sends WhatsApp messages
using the WhatsApp Business Cloud API.

Author: WhatsApp Automation Script
Date: 2024
"""

import pandas as pd
import requests
import json
import time
import logging
from datetime import datetime
from config import WHATSAPP_CONFIG, EXCEL_FILE, LOG_FILE, MESSAGE_DELAY_SECONDS

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class WhatsAppBusinessAPI:
    """WhatsApp Business Cloud API client for sending messages."""
    
    def __init__(self):
        self.phone_number_id = WHATSAPP_CONFIG["PHONE_NUMBER_ID"]
        self.access_token = WHATSAPP_CONFIG["ACCESS_TOKEN"]
        self.api_version = WHATSAPP_CONFIG["API_VERSION"]
        self.country_code = WHATSAPP_CONFIG["COUNTRY_CODE"]
        self.base_url = f"https://graph.facebook.com/{self.api_version}/{self.phone_number_id}/messages"
        
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
    
    def format_phone_number(self, phone):
        """Format phone number with country code."""
        # Remove any spaces, dashes, or special characters
        phone = str(phone).strip().replace(" ", "").replace("-", "").replace("+", "")
        
        # Remove .0 if it's a float from Excel
        if phone.endswith('.0'):
            phone = phone[:-2]
        
        # Add country code if not present
        if not phone.startswith(self.country_code):
            phone = self.country_code + phone
        
        return phone
    
    def send_text_message(self, to_phone, message):
        """
        Send a text message via WhatsApp Business API.
        
        Args:
            to_phone: Recipient's phone number
            message: Text message to send (supports emojis)
        
        Returns:
            dict: API response or error details
        """
        formatted_phone = self.format_phone_number(to_phone)
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": formatted_phone,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message
            }
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                data=json.dumps(payload),
                timeout=30
            )
            
            result = response.json()
            
            if response.status_code == 200:
                message_id = result.get("messages", [{}])[0].get("id", "Unknown")
                logger.info(f"✅ Message sent successfully to {formatted_phone} (ID: {message_id})")
                return {"success": True, "message_id": message_id, "phone": formatted_phone}
            else:
                error = result.get("error", {})
                error_message = error.get("message", "Unknown error")
                error_code = error.get("code", "Unknown")
                logger.error(f"❌ Failed to send to {formatted_phone}: [{error_code}] {error_message}")
                return {"success": False, "error": error_message, "code": error_code, "phone": formatted_phone}
                
        except requests.exceptions.Timeout:
            logger.error(f"❌ Timeout while sending to {formatted_phone}")
            return {"success": False, "error": "Request timeout", "phone": formatted_phone}
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Network error while sending to {formatted_phone}: {str(e)}")
            return {"success": False, "error": str(e), "phone": formatted_phone}
        except Exception as e:
            logger.error(f"❌ Unexpected error: {str(e)}")
            return {"success": False, "error": str(e), "phone": formatted_phone}


def load_contacts_from_excel(file_path):
    """Load contacts from Excel file."""
    try:
        df = pd.read_excel(file_path)
        logger.info(f"📊 Loaded {len(df)} contacts from {file_path}")
        return df
    except FileNotFoundError:
        logger.error(f"❌ Excel file not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"❌ Error reading Excel file: {str(e)}")
        raise


def send_messages_from_excel(excel_file=EXCEL_FILE, test_mode=False, filter_by_date=None):
    """
    Main function to send WhatsApp messages from Excel file.
    
    Args:
        excel_file: Path to the Excel file
        test_mode: If True, only prints what would be sent without actually sending
        filter_by_date: If provided, only send to contacts with this date of birth
    
    Returns:
        dict: Summary of sent messages
    """
    logger.info("=" * 60)
    logger.info("🚀 Starting WhatsApp Message Automation")
    logger.info(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)
    
    # Validate configuration
    if WHATSAPP_CONFIG["PHONE_NUMBER_ID"] == "YOUR_PHONE_NUMBER_ID_HERE":
        logger.error("❌ Please configure your PHONE_NUMBER_ID in config.py")
        return {"error": "Configuration not set"}
    
    if WHATSAPP_CONFIG["ACCESS_TOKEN"] == "YOUR_ACCESS_TOKEN_HERE":
        logger.error("❌ Please configure your ACCESS_TOKEN in config.py")
        return {"error": "Configuration not set"}
    
    # Load contacts
    df = load_contacts_from_excel(excel_file)
    
    # Filter by date if specified
    if filter_by_date:
        df['Date of Birth'] = pd.to_datetime(df['Date of Birth']).dt.date
        filter_date = pd.to_datetime(filter_by_date).date()
        df = df[df['Date of Birth'] == filter_date]
        logger.info(f"🔍 Filtered to {len(df)} contacts with date {filter_by_date}")
    
    if len(df) == 0:
        logger.warning("⚠️ No contacts to process")
        return {"total": 0, "sent": 0, "failed": 0}
    
    # Initialize API client
    api = WhatsAppBusinessAPI()
    
    # Track results
    results = {
        "total": len(df),
        "sent": 0,
        "failed": 0,
        "details": []
    }
    
    # Send messages
    for idx, row in df.iterrows():
        name = row['Name']
        phone = row['Phone']
        message = row['Message']
        
        logger.info(f"\n📤 Processing [{idx + 1}/{len(df)}]: {name}")
        
        if test_mode:
            logger.info(f"   [TEST MODE] Would send to {phone}:")
            logger.info(f"   Message preview: {message[:100]}...")
            results["sent"] += 1
            results["details"].append({"name": name, "phone": phone, "status": "TEST"})
        else:
            result = api.send_text_message(phone, message)
            results["details"].append({
                "name": name,
                "phone": phone,
                "status": "SUCCESS" if result["success"] else "FAILED",
                "details": result
            })
            
            if result["success"]:
                results["sent"] += 1
            else:
                results["failed"] += 1
            
            # Rate limiting - wait between messages
            if idx < len(df) - 1:  # Don't wait after the last message
                logger.info(f"⏳ Waiting {MESSAGE_DELAY_SECONDS} seconds before next message...")
                time.sleep(MESSAGE_DELAY_SECONDS)
    
    # Print summary
    logger.info("\n" + "=" * 60)
    logger.info("📊 SUMMARY")
    logger.info("=" * 60)
    logger.info(f"   Total contacts: {results['total']}")
    logger.info(f"   Successfully sent: {results['sent']}")
    logger.info(f"   Failed: {results['failed']}")
    logger.info("=" * 60)
    
    return results


def send_single_message(phone, message):
    """Send a single message to a specific phone number."""
    api = WhatsAppBusinessAPI()
    return api.send_text_message(phone, message)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='WhatsApp Business API Message Sender')
    parser.add_argument('--test', action='store_true', help='Run in test mode (no actual messages sent)')
    parser.add_argument('--date', type=str, help='Filter by date (YYYY-MM-DD format)')
    parser.add_argument('--file', type=str, default=EXCEL_FILE, help='Path to Excel file')
    
    args = parser.parse_args()
    
    print("\n" + "🟢" * 30)
    print("  WHATSAPP BUSINESS API MESSAGE SENDER")
    print("🟢" * 30 + "\n")
    
    if args.test:
        print("⚠️  RUNNING IN TEST MODE - No messages will be sent\n")
    
    results = send_messages_from_excel(
        excel_file=args.file,
        test_mode=args.test,
        filter_by_date=args.date
    )
    
    print("\n✅ Automation complete!")
