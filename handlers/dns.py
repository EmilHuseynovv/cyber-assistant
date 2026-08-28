from telegram import Update
from telegram.ext import ContextTypes

from services.dns_service import lookup_dns
from utils.validators import validate_domain


async def dns_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage: /dns <domain>\n\n"
            "Example:\n"
            "/dns google.com"
        )
        return

    domain = context.args[0].lower().strip()

    if not validate_domain(domain):
        await update.message.reply_text(
            "❌ Invalid domain name."
        )
        return

    try:
        records = lookup_dns(domain)

        message = (
            "🌐 DNS INTELLIGENCE\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"Domain: {domain}\n\n"
        )

        for record_type, values in records.items():

            message += f"🔹 {record_type} RECORDS\n"

            if values:

                for value in values:
                    message += f"• {value}\n"

            else:
                message += "• Not found\n"

            message += "\n"

        message += "━━━━━━━━━━━━━━━━━━"

        await update.message.reply_text(message)

    except Exception as error:
        print(f"DNS lookup error: {error}")

        await update.message.reply_text(
            "❌ DNS lookup failed."
        )
