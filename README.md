# 📱 WhatsApp Business API Automation

<div align="center">

![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Meta](https://img.shields.io/badge/Meta-0668E1?style=for-the-badge&logo=meta&logoColor=white)

**Automate WhatsApp messages using the official WhatsApp Business Cloud API**

[Getting Started](#-getting-started) • [Features](#-features) • [Usage](#-usage) • [Configuration](#%EF%B8%8F-configuration) • [FAQ](#-faq)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📤 **Bulk Messaging** | Send messages to multiple contacts from an Excel file |
| 🎂 **Birthday Automation** | Filter contacts by date for birthday wishes |
| 🧪 **Test Mode** | Preview messages without actually sending them |
| 📊 **Detailed Logging** | Track all sent messages with timestamps |
| 🔒 **Secure** | Uses official WhatsApp Business Cloud API |
| 🌐 **Emoji Support** | Send messages with emojis and special characters |
| ⏱️ **Rate Limiting** | Built-in delay to avoid API rate limits |

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- ✅ **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
- ✅ **WhatsApp Business Account** ([Sign up](https://business.whatsapp.com/))
- ✅ **Meta for Developers Account** ([Sign up](https://developers.facebook.com/))
- ✅ **Excel file** with contacts (Name, Phone, Message columns)

---

## 🚀 Getting Started

### 1️⃣ Clone or Download the Project

```bash
git clone https://github.com/yourusername/WhatsappAutomation.git
cd WhatsappAutomation
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Credentials

Open `config.py` and fill in your WhatsApp Business API credentials:

```python
WHATSAPP_CONFIG = {
    "PHONE_NUMBER_ID": "YOUR_PHONE_NUMBER_ID_HERE",
    "ACCESS_TOKEN": "YOUR_ACCESS_TOKEN_HERE",
    "API_VERSION": "v18.0",
    "COUNTRY_CODE": "91",  # Change for your country
}
```

> 📖 **Need help getting credentials?** See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions.

### 4️⃣ Prepare Your Excel File

Create an Excel file named `DOBscript.xlsx` with the following format:

| Name | Date of Birth | Phone | Message |
|------|---------------|-------|---------|
| John Doe | 2025-12-25 | 9876543210 | 🎂 Happy Birthday, John! |
| Jane Smith | 2025-12-26 | 9123456789 | 🎉 Wishing you a wonderful day! |

---

## 💻 Usage

### Test Mode (Recommended for First Run)

Preview which messages would be sent without actually sending:

```bash
python whatsapp_sender.py --test
```

### Send Messages to All Contacts

```bash
python whatsapp_sender.py
```

### Filter by Date

Send only to contacts with a specific date of birth:

```bash
python whatsapp_sender.py --date 2025-12-25
```

### Use a Different Excel File

```bash
python whatsapp_sender.py --file path/to/your/contacts.xlsx
```

### Combine Options

```bash
python whatsapp_sender.py --file contacts.xlsx --date 2025-12-25 --test
```

---

## ⚙️ Configuration

All configuration options are in `config.py`:

| Setting | Description | Default |
|---------|-------------|---------|
| `PHONE_NUMBER_ID` | Your WhatsApp Phone Number ID from Meta | Required |
| `ACCESS_TOKEN` | Your API access token | Required |
| `API_VERSION` | WhatsApp API version | `v18.0` |
| `COUNTRY_CODE` | Default country code for phone numbers | `91` (India) |
| `EXCEL_FILE` | Default Excel file to read contacts from | `DOBscript.xlsx` |
| `LOG_FILE` | Log file for tracking messages | `whatsapp_automation.log` |
| `MESSAGE_DELAY_SECONDS` | Delay between messages (rate limiting) | `2` seconds |

---

## 📁 Project Structure

```
WhatsappAutomation/
├── 📄 README.md            # This file
├── 📄 SETUP_GUIDE.md       # Detailed setup instructions
├── 🐍 whatsapp_sender.py   # Main automation script
├── ⚙️ config.py            # API credentials & settings
├── 📦 requirements.txt     # Python dependencies
├── 📊 DOBscript.xlsx       # Your contact list (create this)
└── 📋 whatsapp_automation.log  # Log file (auto-created)
```

---

## 📊 Excel File Format

Your Excel file must have these columns:

| Column | Description | Example |
|--------|-------------|---------|
| **Name** | Contact's name | John Doe |
| **Date of Birth** | DOB for filtering | 2025-12-25 |
| **Phone** | 10-digit phone number | 9876543210 |
| **Message** | Message to send (supports emojis) | 🎂 Happy Birthday! |

### Tips for Messages

- Use emojis! 🎉🎂🎁
- For line breaks in Excel, use `Alt + Enter`
- Keep messages under 4096 characters

---

## ⚠️ Important Notes

### Rate Limits
- WhatsApp has API rate limits
- Default delay is 2 seconds between messages
- Increase `MESSAGE_DELAY_SECONDS` if you hit rate limits

### Development vs Production Mode

| Mode | Capability |
|------|------------|
| **Development** | Only message pre-registered test numbers |
| **Production** | Message any WhatsApp user (requires business verification) |

### Message Templates
For messaging users who haven't messaged you first, you need **approved message templates**. See [SETUP_GUIDE.md](SETUP_GUIDE.md) for details.

---

## 🔧 Troubleshooting

| Error | Solution |
|-------|----------|
| `Invalid OAuth 2.0 Access Token` | Token expired, generate a new one |
| `Phone number not registered` | Recipient isn't on WhatsApp |
| `Rate limit exceeded` | Increase `MESSAGE_DELAY_SECONDS` and wait |
| `Configuration not set` | Update credentials in `config.py` |
| `Excel file not found` | Check file path and name |

---

## 📖 Documentation

- 📘 [SETUP_GUIDE.md](SETUP_GUIDE.md) - Complete setup walkthrough
- 📗 [WhatsApp Cloud API Docs](https://developers.facebook.com/docs/whatsapp/cloud-api)
- 📙 [Meta Business Help Center](https://www.facebook.com/business/help/whatsapp)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Built with the [WhatsApp Business Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api)
- Powered by [Meta for Developers](https://developers.facebook.com/)

---

<div align="center">

**Made with ❤️ for GNH**

</div>
