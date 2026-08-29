# 🛡️ Cyber Assistant

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

| Module | Description |
|---|---|
| 🌐 **IP Intelligence** | Gather available information about an IP address |
| 🔎 **DNS Lookup** | Query DNS records for domains and hostnames |
| 📡 **Nmap Scanner** | Scan authorized targets and identify ports/services |
| 🛡️ **AbuseIPDB** | Check IP reputation and abuse reports |
| 🔐 **Password Utilities** | Security-focused password utilities |

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

## 🧰 Tech Stack

<p align="center">

<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
</a>

<a href="https://python-telegram-bot.org/">
  <img src="https://img.shields.io/badge/python--telegram--bot-26A5E4?style=flat-square&logo=telegram&logoColor=white">
</a>

<a href="https://nmap.org/">
  <img src="https://img.shields.io/badge/Nmap-4682B4?style=flat-square">
</a>

<a href="https://www.abuseipdb.com/">
  <img src="https://img.shields.io/badge/AbuseIPDB-000000?style=flat-square">
</a>

<a href="https://www.linux.org/">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black">
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
