# 🛡️ Cyber Assistant

<div data-importer="image" align="center">
  <img data-importer="image" height="150" src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXk5NDZtNjhuY2R1dGt2MGwwa2txMTdpMHZvOXoyZ3FsMTIyNzVsaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QNFhOolVeCzPQ2Mx85/giphy.gif"  />
</div>

###

<p align="center">
  <strong>A practical cybersecurity toolkit — directly inside Telegram.</strong>
</p>

<p align="center">
  <a href="https://t.me/cyberassistant_hs_bot">
    <img src="https://img.shields.io/badge/Telegram-Open%20Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Open Telegram Bot">
  </a>
  <a href="https://github.com/EmilHuseynovv/cyber-assistant">
    <img src="https://img.shields.io/github/stars/EmilHuseynovv/cyber-assistant?style=for-the-badge" alt="GitHub Stars">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

<p align="center">
  <img src="assets/banner.png" alt="Cyber Assistant Banner" width="850">
</p>

---

## ⚡ What is Cyber Assistant?

**Cyber Assistant** is a Telegram-based cybersecurity assistant built with Python.

It brings several practical security and network-analysis utilities into one interface, allowing users to perform common reconnaissance and diagnostic tasks without leaving Telegram.

> 🎯 Built for cybersecurity learning, network analysis, and authorized security testing.

---

## 🚀 Features

<table>
<tr>
<td width="50%">

### 🌐 IP Intelligence

Retrieve available information about an IP address and inspect network and security-related data.

</td>
<td width="50%">

### 🔎 DNS Lookup

Query DNS information for domains and hostnames.

</td>
</tr>

<tr>
<td width="50%">

### 📡 Nmap Scanner

Run Nmap-based scans against authorized targets and identify available ports and services.

</td>
<td width="50%">

### 🛡️ AbuseIPDB

Check IP reputation and available abuse reports through AbuseIPDB.

</td>
</tr>

<tr>
<td width="50%">

### 🔐 Password Utilities

Security-focused password utilities designed for testing and learning.

</td>
<td width="50%">

### 🤖 Telegram Interface

Access the tools through a simple Telegram bot interface without requiring a separate web dashboard.

</td>
</tr>
</table>

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/EmilHuseynovv/cyber-assistant.git
cd cyber-assistant
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create your `.env` file:

```bash
cp .env.example .env
```

Then configure:

```env
BOT_TOKEN=your_telegram_bot_token
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
```

### 5. Run the bot

```bash
python3 bot.py
```

---

## 🤖 Try the Bot

<p align="center">
  <a href="https://t.me/cyberassistant_hs_bot">
    <img src="https://img.shields.io/badge/🚀%20OPEN%20CYBER%20ASSISTANT-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Open Cyber Assistant">
  </a>
</p>

---

## 📸 Preview

### 🏠 Main Menu

<p align="center">
  <img src="assets/start.png" width="300">
</p>

### 🌐 IP Intelligence

<p align="center">
  <img src="assets/ip-intelligence.png" width="300">
</p>

### 🔎 DNS Lookup

<p align="center">
  <img src="assets/dns-lookup.png" width="300">
</p>

### 📡 Nmap Scan

<p align="center">
  <img src="assets/nmap-scan.png" width="300">
</p>

---

### Architecture

| Directory / File | Purpose                                      |
| ---------------- | -------------------------------------------- |
| `handlers/`      | Telegram commands and user interactions      |
| `services/`      | Core logic and external API integrations     |
| `utils/`         | Validation, formatting, and helper functions |
| `bot.py`         | Application entry point                      |
| `config.py`      | Environment configuration and secret loading |

---

## 🧰 Tech Stack

<p align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50" alt="Python" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.linux.org/" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="50" alt="Linux" />
  </a>
  &nbsp;&nbsp;
  <a href="https://core.telegram.org/bots/api" target="_blank">
    <img src="https://cdn.simpleicons.org/telegram/26A5E4" height="50" alt="Telegram Bot API" />
  </a>
  &nbsp;&nbsp;
  <a href="https://nmap.org/" target="_blank">
    <img src="https://cdn.simpleicons.org/nmap/4682B4" height="50" alt="Nmap" />
  </a>
  &nbsp;&nbsp;
  <a href="https://git-scm.com/" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="50" alt="Git" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" height="50" alt="GitHub" />
  </a>
</p>

---

## 📂 Project Structure

```text
cyber-assistant/
│
├── assets/
│   ├── banner.png
│   ├── start.png
│   ├── ip-intelligence.png
│   ├── dns-lookup.png
│   └── nmap-scan.png
│
├── handlers/
│   ├── start.py
│   ├── ip.py
│   ├── dns.py
│   ├── scan.py
│   └── password.py
│
├── services/
│   ├── ip_service.py
│   ├── dns_service.py
│   ├── scan_service.py
│   └── password_service.py
│
├── utils/
│   ├── formatters.py
│   └── validators.py
│
├── bot.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md

