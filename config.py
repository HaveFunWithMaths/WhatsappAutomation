"""
WhatsApp Business API Configuration
====================================
Fill in your credentials from the Meta for Developers dashboard.

SETUP INSTRUCTIONS:
1. Go to https://developers.facebook.com/
2. Create or select your app
3. Add WhatsApp product to your app
4. Get your Phone Number ID and Access Token from the API Setup page
5. Fill in the values below
"""

# Your WhatsApp Business API credentials
WHATSAPP_CONFIG = {
    # Your Phone Number ID from Meta Business Suite
    # Found at: Facebook App Dashboard > WhatsApp > API Setup > Phone number ID
    "PHONE_NUMBER_ID": "YOUR_PHONE_NUMBER_ID_HERE",
    
    # Your permanent access token
    # Get it from: Facebook App Dashboard > WhatsApp > API Setup > Permanent Token
    # Or generate a temporary one that lasts 24 hours
    "ACCESS_TOKEN": "YOUR_ACCESS_TOKEN_HERE",
    
    # API Version (latest stable version)
    "API_VERSION": "v18.0",
    
    # Country code for phone numbers (India = 91)
    "COUNTRY_CODE": "91",
}

# Path to your Excel file
EXCEL_FILE = "DOBscript.xlsx"

# Logging settings
LOG_FILE = "whatsapp_automation.log"

# Rate limiting (WhatsApp has limits on messages per second)
# Recommended: Wait 1-2 seconds between messages to avoid rate limits
MESSAGE_DELAY_SECONDS = 2
