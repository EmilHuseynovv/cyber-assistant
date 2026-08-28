import requests

from config import ABUSEIPDB_API_KEY


def lookup_ip(ip: str) -> dict:
    response = requests.get(
        f"https://ipinfo.io/{ip}/json",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def check_ip_reputation(ip: str) -> dict:
    response = requests.get(
        "https://api.abuseipdb.com/api/v2/check",
        headers={
            "Key": ABUSEIPDB_API_KEY,
            "Accept": "application/json"
        },
        params={
            "ipAddress": ip,
            "maxAgeInDays": 90
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()["data"]
