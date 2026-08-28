import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN

from handlers.start import (
    start,
    button_handler
)

from handlers.ip import ip_lookup
from handlers.dns import dns_lookup
from handlers.scan import port_scan

from handlers.password import (
    password_start,
    password_analyze
)


logging.basicConfig(
    format=(
        "%(asctime)s - "
        "%(name)s - "
        "%(levelname)s - "
        "%(message)s"
    ),
    level=logging.INFO
)


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    logging.error(
        "Exception while handling update:",
        exc_info=context.error
    )


def main():

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Commands
    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("ip", ip_lookup)
    )

    app.add_handler(
        CommandHandler("dns", dns_lookup)
    )

    app.add_handler(
        CommandHandler("scan", port_scan)
    )

    app.add_handler(
        CommandHandler(
            "password",
            password_start
        )
    )

    # Buttons
    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )

    # Password input
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            password_analyze
        )
    )

    # Error handling
    app.add_error_handler(
        error_handler
    )

    print("🛡️ Cyber Assistant started...")

    app.run_polling()


if __name__ == "__main__":
    main()
