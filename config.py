import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN is not configured in .env"
    )

if not ABUSEIPDB_API_KEY:
    raise RuntimeError(
        "ABUSEIPDB_API_KEY is not configured in .env"
    )
