# 🛡️ Cyber Assistant

<div data-importer="image" align="center">
  <img data-importer="image" height="150" src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXk5NDZtNjhuY2R1dGt2MGwwa2txMTdpMHZvOXoyZ3FsMTIyNzVsaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QNFhOolVeCzPQ2Mx85/giphy.gif"  />
</div>

<p align="center">
  <strong>A practical cybersecurity toolkit — directly inside Telegram.</strong>
</p>

<p align="center">
  <a href="https://t.me/cyberassistant_hs_bot">
    <img src="https://img.shields.io/badge/🚀_Open_Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Open Cyber Assistant">
  </a>
  <a href="https://github.com/EmilHuseynovv/cyber-assistant">
    <img src="https://img.shields.io/github/stars/EmilHuseynovv/cyber-assistant?style=for-the-badge&logo=github" alt="GitHub Stars">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

---

## ⚡ About

**Cyber Assistant** is a Python-based Telegram bot that combines practical cybersecurity and network-analysis utilities into one interface.

It is designed for cybersecurity learning, network diagnostics, and **authorized security testing**.

---

## 🚀 Features

| Tool                      | Purpose                                                 |
| ------------------------- | ------------------------------------------------------- |
| 🌐 **IP Intelligence**    | Retrieve available information about an IP address      |
| 🔎 **DNS Lookup**         | Query DNS information for domains and hostnames         |
| 📡 **Nmap Scanner**       | Scan authorized targets and identify ports and services |
| 🛡️ **AbuseIPDB**         | Check IP reputation and abuse reports                   |
| 🔐 **Password Utilities** | Security-focused password utilities                     |

---

## 🤖 Try the Bot

### [🚀 Open Cyber Assistant on Telegram](https://t.me/cyberassistant_hs_bot)

**Bot:** [@cyberassistant_hs_bot](https://t.me/cyberassistant_hs_bot)

---

## 📸 Screenshots

### 🏠 Main Menu

![Cyber Assistant Start Menu](assets/start.png)

### 🌐 IP Intelligence

![IP Intelligence](assets/ip-intelligence.png)

### 🔎 DNS Lookup

![DNS Lookup](assets/dns-lookup.png)

### 📡 Nmap Scan

![Nmap Scan](assets/nmap-scan.png)

---

## 🧰 Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram%20Bot%20API-26A5E4?style=for-the-badge\&logo=telegram\&logoColor=white)](https://core.telegram.org/bots/api)
[![Nmap](https://img.shields.io/badge/Nmap-4682B4?style=for-the-badge)](https://nmap.org/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge\&logo=linux\&logoColor=black)](https://www.linux.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)](https://git-scm.com/)

**Core:** Python · python-telegram-bot · Requests · python-dotenv
**Security:** Nmap · AbuseIPDB
**Environment:** Linux / Kali Linux

---

## 📂 Project Structure

```text
cyber-assistant/
├── assets/
│   ├── start.png
│   ├── ip-intelligence.png
│   ├── dns-lookup.png
│   └── nmap-scan.png
│
├── handlers/
│   ├── __init__.py
│   ├── start.py
│   ├── ip.py
│   ├── dns.py
│   ├── scan.py
│   └── password.py
│
├── services/
│   ├── __init__.py
│   ├── ip_service.py
│   ├── dns_service.py
│   ├── scan_service.py
│   └── password_service.py
│
├── utils/
│   ├── __init__.py
│   ├── formatters.py
│   └── validators.py
│
├── bot.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/EmilHuseynovv/cyber-assistant.git
cd cyber-assistant
```

### Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```bash
cp .env.example .env
```

Add your credentials:

```env
BOT_TOKEN=your_telegram_bot_token
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
```

### Run the bot

```bash
python3 bot.py
```

---

## 🔐 Security & Responsible Use

Cyber Assistant is intended for:

* ✅ Cybersecurity education
* ✅ Network diagnostics
* ✅ Authorized security testing
* ✅ Lab environments

Do **not** scan, enumerate, or analyze systems without explicit permission.

Never commit:

```text
.env
BOT_TOKEN
ABUSEIPDB_API_KEY
```

---

## 🗺️ Roadmap

* [ ] WHOIS lookup
* [ ] Subdomain enumeration
* [ ] URL analysis
* [ ] Improved Nmap reports
* [ ] Expanded IP intelligence
* [ ] Additional OSINT utilities
* [ ] Better logging and error handling
* [ ] Automated tests
* [ ] GitHub Actions / CI
* [ ] User preferences

---

## 🤝 Contributing

Suggestions, bug reports, and contributions are welcome.

For major changes, please open an issue first to discuss the proposed change.

---

## 📄 License

Released under the **MIT License**.

---

## 👨‍💻 Author

**Emil Huseynov**

[![GitHub](https://img.shields.io/badge/GitHub-EmilHuseynovv-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/EmilHuseynovv)

---

<p align="center">
  <strong>Built with 🐍 Python • 🤖 Telegram • 🛡️ Cybersecurity</strong>
</p>
