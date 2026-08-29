🛡️ Cyber Assistant

A Telegram bot built with Python for practical cybersecurity and network-analysis utilities.

Cyber Assistant brings several security-focused tools into a single Telegram interface, including IP intelligence, DNS lookups, network scanning, and password utilities.

✨ Features

🌐 IP Intelligence — inspect an IP address and retrieve available network/security information.

🔎 DNS Lookup — query DNS information for a domain or hostname.

📡 Network Scanning — run Nmap-based scans against authorized targets.

🔐 Password Utilities — password-related generation/checking utilities.

⚙️ Environment-based configuration — secrets are loaded from a local .env file instead of being hard-coded.

🧰 Tech Stack

Python 3

python-telegram-bot

Nmap

AbuseIPDB API

python-dotenv

📁 Project Structure

cyber-assistant/
├── bot.py
├── config.py
├── requirements.txt
├── .gitignore
├── handlers/
│   ├── __init__.py
│   ├── dns.py
│   ├── ip.py
│   ├── password.py
│   ├── scan.py
│   └── start.py
├── services/
│   ├── __init__.py
│   ├── dns_service.py
│   ├── ip_service.py
│   ├── password_service.py
│   └── scan_service.py
└── utils/
    ├── __init__.py
    ├── formatters.py
    └── validators.py

🚀 Installation

1. Clone the repository

git clone https://github.com/EmilHuseynovv/cyber-assistant.git
cd cyber-assistant

2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Install Nmap

On Kali Linux:

sudo apt update
sudo apt install nmap -y

5. Configure environment variables

Create a .env file in the project root:

BOT_TOKEN=your_telegram_bot_token
ABUSEIPDB_API_KEY=your_abuseipdb_api_key

Never commit .env or real API keys to GitHub.

6. Start the bot

python3 bot.py

🤖 Usage

Open the bot in Telegram and use the available commands/features exposed by the bot's handlers.

Typical functionality includes:

/start    Start the bot
/ip       IP intelligence
/dns      DNS lookup
/scan     Nmap/network scan
/password Password utilities

The exact command arguments and interaction flow may depend on the current implementation in the corresponding handlers/ modules.

🔒 Security & Responsible Use

Cyber Assistant is intended for authorized security testing, defensive research, and educational use.

Only scan or investigate systems and IP addresses that you own or have explicit permission to test. Do not use the bot to perform unauthorized reconnaissance, scanning, or attacks.

Keep secrets out of source control:

.env should remain local.

API keys and bot tokens must never be hard-coded.

Rotate any credential that is accidentally exposed.

🛠️ Development

The project separates Telegram handlers from service/business logic:

handlers/ — Telegram commands and user interaction.

services/ — core functionality and external API/tool integration.

utils/ — validation and response formatting.

config.py — environment-based configuration.

bot.py — application entry point.

After making changes:

git add .
git commit -m "Describe your change"
git push

📌 Roadmap

Possible future improvements:

Multi-language responses (Azerbaijani, English, Russian, Turkish)

More threat-intelligence integrations

Improved scan result formatting

Logging and better error handling

Role-based/admin features

Unit tests and automated CI

⚠️ Disclaimer

This project is provided for educational and authorized security purposes. The author is not responsible for misuse of the software.

👨‍💻 Author

Emil Huseynov

GitHub: @EmilHuseynovv
