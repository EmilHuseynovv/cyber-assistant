from telegram import Update
from telegram.ext import ContextTypes

from services.scan_service import run_nmap_scan
from utils.validators import validate_ip
from utils.formatters import truncate_text


async def port_scan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage: /scan <IP address>\n\n"
            "Example:\n"
            "/scan 127.0.0.1"
        )
        return

    target = context.args[0]

    if not validate_ip(target):
        await update.message.reply_text(
            "❌ Invalid IP address."
        )
        return

    await update.message.reply_text(
        "🔎 Starting Nmap service scan...\n\n"
        f"Target: {target}\n"
        "Method: Nmap -sV"
    )

    try:

        output = run_nmap_scan(target)

        if not output.strip():
            await update.message.reply_text(
                "🔴 No results found."
            )
            return

        output = truncate_text(output)

        message = (
            "🔎 NMAP SERVICE SCAN\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"Target: {target}\n\n"
            f"```text\n{output}\n```"
        )

        await update.message.reply_text(
            message,
            parse_mode="Markdown"
        )

    except TimeoutError:

        await update.message.reply_text(
            "⏱️ Scan timed out."
        )

    except Exception as error:

        print(f"Nmap error: {error}")

        await update.message.reply_text(
            "❌ Nmap scan failed."
        )
