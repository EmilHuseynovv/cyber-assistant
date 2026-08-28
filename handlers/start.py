from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import ContextTypes


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [
        [
            InlineKeyboardButton(
                "🌐 IP Intelligence",
                callback_data="ip_help"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 DNS Intelligence",
                callback_data="dns_help"
            )
        ],
        [
            InlineKeyboardButton(
                "🔎 Network Scanner",
                callback_data="scan_help"
            )
        ],
        [
            InlineKeyboardButton(
                "🔐 Password Security",
                callback_data="password_help"
            )
        ],
        [
            InlineKeyboardButton(
                "ℹ️ Help",
                callback_data="help"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(
        keyboard
    )

    await update.message.reply_text(
        "🛡️ CYBER ASSISTANT\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Welcome to Cyber Assistant.\n\n"
        "Select a security tool below:",
        reply_markup=reply_markup
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    responses = {

        "ip_help":
            "🌐 IP Intelligence\n\n"
            "Usage:\n"
            "/ip 8.8.8.8",

        "dns_help":
            "🌍 DNS Intelligence\n\n"
            "Usage:\n"
            "/dns google.com",

        "scan_help":
            "🔎 Network Scanner\n\n"
            "Usage:\n"
            "/scan 127.0.0.1\n\n"
            "⚠️ Scan only systems you own "
            "or have permission to test.",

        "password_help":
            "🔐 Password Security\n\n"
            "Usage:\n"
            "/password\n\n"
            "The password is analyzed locally "
            "and is not sent to external APIs.",

        "help":
            "ℹ️ COMMANDS\n\n"
            "/start — Main menu\n"
            "/ip — IP Intelligence\n"
            "/dns — DNS Intelligence\n"
            "/scan — Nmap Scanner\n"
            "/password — Password Security"
    }

    await query.edit_message_text(
        responses.get(
            query.data,
            "Unknown option."
        )
    )
