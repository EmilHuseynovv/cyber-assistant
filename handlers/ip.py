import ipaddress

from telegram import Update
from telegram.ext import ContextTypes

from services.ip_service import (
    lookup_ip,
    check_ip_reputation,
)

from utils.validators import validate_ip


async def ip_lookup(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    # ─────────────────────────────────────────
    # CHECK ARGUMENT
    # ─────────────────────────────────────────

    if not context.args:
        await update.message.reply_text(
            "🌐 IP INTELLIGENCE\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Usage:\n"
            "/ip <IP address>\n\n"
            "Example:\n"
            "/ip 8.8.8.8"
        )
        return

    ip = context.args[0].strip()

    # ─────────────────────────────────────────
    # VALIDATE IP
    # ─────────────────────────────────────────

    if not validate_ip(ip):
        await update.message.reply_text(
            "❌ INVALID IP ADDRESS\n\n"
            "Please enter a valid IPv4 or IPv6 address."
        )
        return

    # ─────────────────────────────────────────
    # IP CLASSIFICATION
    # ─────────────────────────────────────────

    try:
        ip_obj = ipaddress.ip_address(ip)

    except ValueError:
        await update.message.reply_text(
            "❌ INVALID IP ADDRESS"
        )
        return

    # ─────────────────────────────────────────
    # PRIVATE / NON-PUBLIC IP
    # ─────────────────────────────────────────

    if (
        ip_obj.is_private
        or ip_obj.is_loopback
        or ip_obj.is_reserved
        or ip_obj.is_link_local
    ):

        if ip_obj.is_loopback:
            ip_type = "LOOPBACK 🔄"

        elif ip_obj.is_link_local:
            ip_type = "LINK-LOCAL 🔗"

        elif ip_obj.is_reserved:
            ip_type = "RESERVED ⚠️"

        else:
            ip_type = "PRIVATE 🔒"

        await update.message.reply_text(
            "🌐 IP INTELLIGENCE\n"
            "━━━━━━━━━━━━━━━━━━\n\n"

            "📍 IP ADDRESS\n"
            f"{ip}\n\n"

            "🔐 IP TYPE\n"
            f"{ip_type}\n\n"

            "ℹ️ This IP address is not publicly "
            "routable on the Internet.\n\n"

            "🌍 GEOLOCATION\n"
            "Not available\n\n"

            "🏢 NETWORK\n"
            "Local / Reserved network\n\n"

            "🛡️ THREAT INTELLIGENCE\n"
            "Skipped\n\n"

            "Reason: Non-public IP address\n\n"

            "━━━━━━━━━━━━━━━━━━"
        )

        return

    # ─────────────────────────────────────────
    # PUBLIC IP
    # ─────────────────────────────────────────

    status_message = await update.message.reply_text(
        "🔎 IP INTELLIGENCE\n\n"
        f"Analyzing: {ip}\n"
        "Please wait..."
    )

    try:

        # ─────────────────────────────────────
        # IPINFO
        # ─────────────────────────────────────

        data = lookup_ip(ip)

        # ─────────────────────────────────────
        # ABUSEIPDB
        # ─────────────────────────────────────

        try:

            reputation = check_ip_reputation(ip)

            reputation_available = True

        except Exception as error:

            print(
                f"AbuseIPDB error: {error}"
            )

            reputation = {}

            reputation_available = False

        # ─────────────────────────────────────
        # BASIC INFORMATION
        # ─────────────────────────────────────

        ip_address = data.get(
            "ip",
            ip
        )

        country = data.get(
            "country",
            "Unknown"
        )

        region = data.get(
            "region",
            "Unknown"
        )

        city = data.get(
            "city",
            "Unknown"
        )

        timezone = data.get(
            "timezone",
            "Unknown"
        )

        coordinates = data.get(
            "loc",
            "Unknown"
        )

        organization = data.get(
            "org",
            "Unknown"
        )

        hostname = data.get(
            "hostname",
            "Unknown"
        )

        # ─────────────────────────────────────
        # THREAT INTELLIGENCE
        # ─────────────────────────────────────

        if reputation_available:

            abuse_score = reputation.get(
                "abuseConfidenceScore",
                "Unknown"
            )

            total_reports = reputation.get(
                "totalReports",
                "Unknown"
            )

            last_reported = reputation.get(
                "lastReportedAt",
                "Never"
            )

            is_whitelisted = reputation.get(
                "isWhitelisted",
                "Unknown"
            )

            if is_whitelisted is True:
                whitelist_text = "Yes"

            elif is_whitelisted is False:
                whitelist_text = "No"

            else:
                whitelist_text = "Unknown"

        else:

            abuse_score = "Unavailable"

            total_reports = "Unavailable"

            last_reported = "Unavailable"

            whitelist_text = "Unavailable"

        # ─────────────────────────────────────
        # RISK LEVEL
        # ─────────────────────────────────────

        if isinstance(
            abuse_score,
            int
        ):

            if abuse_score == 0:

                risk = "LOW 🟢"

            elif abuse_score < 25:

                risk = "LOW 🟢"

            elif abuse_score < 50:

                risk = "MEDIUM 🟡"

            elif abuse_score < 75:

                risk = "HIGH 🟠"

            else:

                risk = "CRITICAL 🔴"

        else:

            risk = "UNKNOWN ⚪"

        # ─────────────────────────────────────
        # FINAL REPORT
        # ─────────────────────────────────────

        message = (
            "🌐 IP INTELLIGENCE\n"
            "━━━━━━━━━━━━━━━━━━\n\n"

            "📍 IP ADDRESS\n"
            f"{ip_address}\n\n"

            "🔐 IP TYPE\n"
            "PUBLIC 🌍\n\n"

            "🌍 GEOLOCATION\n"
            f"Country: {country}\n"
            f"Region: {region}\n"
            f"City: {city}\n"
            f"Timezone: {timezone}\n"
            f"Coordinates: {coordinates}\n\n"

            "🏢 NETWORK\n"
            f"Organization: {organization}\n"
            f"Hostname: {hostname}\n\n"

            "🛡️ THREAT INTELLIGENCE\n"
            f"Risk Level: {risk}\n"
            f"Abuse Score: {abuse_score}%\n"
            f"Reports: {total_reports}\n"
            f"Last Reported: {last_reported}\n"
            f"Whitelisted: {whitelist_text}\n\n"

            "🔒 PRIVACY\n"
            "No IP data is stored by "
            "Cyber Assistant.\n\n"

            "━━━━━━━━━━━━━━━━━━"
        )

        await status_message.edit_text(
            message
        )

    # ─────────────────────────────────────────
    # ERROR HANDLING
    # ─────────────────────────────────────────

    except Exception as error:

        print(
            f"IP intelligence error: {error}"
        )

        await status_message.edit_text(
            "❌ IP INTELLIGENCE FAILED\n"
            "━━━━━━━━━━━━━━━━━━\n\n"

            "Unable to retrieve information "
            "for this IP address.\n\n"

            "Please try again later."
        )
