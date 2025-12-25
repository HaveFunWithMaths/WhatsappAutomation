# WhatsApp Business API Automation - Setup Guide

## 📋 Prerequisites

1. **WhatsApp Business Account** - You need a verified WhatsApp Business account
2. **Meta for Developers Account** - Sign up at [developers.facebook.com](https://developers.facebook.com/)
3. **Python 3.8+** installed on your computer

---

## 🚀 Step-by-Step Setup

### Step 1: Create a Meta App

1. Go to [Meta for Developers](https://developers.facebook.com/)
2. Click **"My Apps"** → **"Create App"**
3. Select **"Business"** as the app type
4. Fill in the app name (e.g., "WhatsApp Automation")
5. Select your Business Account (or create one)
6. Click **"Create App"**

### Step 2: Add WhatsApp Product

1. In your app dashboard, scroll down to **"Add Products"**
2. Find **"WhatsApp"** and click **"Set Up"**
3. You'll be redirected to the WhatsApp API Setup page

### Step 3: Get Your API Credentials

1. In the WhatsApp Setup page, you'll see:
   - **Phone number ID** - Copy this number
   - **WhatsApp Business Account ID** - Note this for reference
   
2. Scroll down to **"Temporary access token"**:
   - Click **"Generate"** to get a token (valid for 24 hours)
   - For permanent access, see Step 5 below

### Step 4: Configure Your Script

1. Open `config.py` in a text editor
2. Replace the placeholder values:

```python
WHATSAPP_CONFIG = {
    "PHONE_NUMBER_ID": "1234567890123456",  # Your actual Phone Number ID
    "ACCESS_TOKEN": "EAAxxxxxx...",          # Your access token
    "API_VERSION": "v18.0",
    "COUNTRY_CODE": "91",  # India country code
}
```

### Step 5: Generate a Permanent Access Token (Recommended)

Temporary tokens expire in 24 hours. For a permanent token:

1. Go to [Meta Business Suite](https://business.facebook.com/)
2. Navigate to **Settings** → **Business Settings**
3. Select **System Users** → **Add** (create a new system user)
4. Give it a name and set role to **Admin**
5. Click on the system user → **Add Assets**
6. Add your WhatsApp Business Account with full control
7. Click **Generate New Token**
8. Select your app and these permissions:
   - `whatsapp_business_management`
   - `whatsapp_business_messaging`
9. Click **Generate Token** and save it securely!

### Step 6: Add Test Phone Numbers (Development Mode)

While in development mode, you can only message phone numbers you've added:

1. In the WhatsApp Setup page, find **"To"** field
2. Click **"Manage phone number list"**
3. Add the phone numbers you want to test with
4. Each phone number will receive a verification code via WhatsApp

### Step 7: Install Python Dependencies

Open Command Prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

---

## 🎯 Running the Script

### Test Mode (Recommended First)
Run without actually sending messages:
```bash
python whatsapp_sender.py --test
```

### Send Messages
Send messages to all contacts in the Excel file:
```bash
python whatsapp_sender.py
```

### Filter by Date
Send only to contacts with a specific date:
```bash
python whatsapp_sender.py --date 2025-12-06
```

### Use Different Excel File
```bash
python whatsapp_sender.py --file another_file.xlsx
```

---

## 📊 Excel File Format

Your Excel file should have these columns:
| Name | Date of Birth | Phone | Message |
|------|---------------|-------|---------|
| John | 2025-12-06 | 9876543210 | 🎂 Happy Birthday! |

- **Phone numbers**: 10-digit Indian numbers (country code is added automatically)
- **Messages**: Support emojis and newlines (use `\n` for new lines)

---

## ⚠️ Important Notes

### Rate Limits
- WhatsApp Business API has rate limits
- The script waits 2 seconds between messages (configurable in `config.py`)
- Don't exceed 1,000 messages per phone number per day

### Message Templates (For Business Accounts)
If you're sending to users who haven't messaged you first, you need:
1. Approved message templates
2. Use template messages instead of freeform text

For template messages, modify `whatsapp_sender.py` to use:
```python
payload = {
    "messaging_product": "whatsapp",
    "to": formatted_phone,
    "type": "template",
    "template": {
        "name": "your_template_name",
        "language": {"code": "en"}
    }
}
```

### Going to Production
1. Complete Facebook's Business Verification
2. Add a real business phone number
3. Get your message templates approved
4. Apply for API access upgrade

---

## 🔧 Troubleshooting

### "Invalid OAuth 2.0 Access Token"
- Your token has expired, generate a new one

### "Phone number not registered"
- The recipient's phone number is not on WhatsApp

### "Message failed to send"
- Check if the phone number is in your test list (development mode)
- Verify the phone number format is correct

### "Rate limit exceeded"
- Wait a few minutes and try again
- Increase `MESSAGE_DELAY_SECONDS` in `config.py`

---

## 📁 Project Files

```
WhatsappAutomation/
├── config.py              # Your API credentials (EDIT THIS!)
├── whatsapp_sender.py     # Main automation script
├── DOBscript.xlsx         # Your contact list
├── requirements.txt       # Python dependencies
├── whatsapp_automation.log # Log file (created after running)
└── SETUP_GUIDE.md         # This guide
```

---

## 🆘 Need Help?

- [WhatsApp Business API Docs](https://developers.facebook.com/docs/whatsapp/cloud-api)
- [Meta for Developers](https://developers.facebook.com/)
- [WhatsApp Business Help Center](https://www.facebook.com/business/help/whatsapp)
