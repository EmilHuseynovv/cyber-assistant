from telegram import Update
from telegram.ext import ContextTypes

from services.password_service import analyze_password


async def delete_password_result(context):
    data = context.job.data

    try:
        await context.bot.delete_message(
            chat_id=data["chat_id"],
            message_id=data["message_id"]
        )

    except Exception as error:
        print(
            f"Could not delete password result: {error}"
        )


async def password_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["waiting_for_password"] = True

    await update.message.reply_text(
        "🔐 PASSWORD SECURITY CHECKER\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "Send your password in the next message.\n\n"

        "🔒 PRIVACY\n"
        "• Processed locally\n"
        "• Not stored\n"
        "• Not sent to external APIs\n"
        "• Your password message will be deleted\n\n"

        "⚠️ Do not send a password that you currently "
        "use for an important account."
    )


async def password_analyze(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not context.user_data.get(
        "waiting_for_password"
    ):
        return

    if not update.message or not update.message.text:
        return

    password = update.message.text

    context.user_data["waiting_for_password"] = False

    # Delete password message immediately
    try:
        await update.message.delete()

    except Exception as error:
        print(
            f"Could not delete password message: {error}"
        )

    # Local analysis
    result = analyze_password(password)

    recommendations = []

    if result["length"] < 12:
        recommendations.append(
            "Use at least 12 characters."
        )

    if not result["upper"]:
        recommendations.append(
            "Add uppercase letters."
        )

    if not result["lower"]:
        recommendations.append(
            "Add lowercase letters."
        )

    if not result["digit"]:
        recommendations.append(
            "Add numbers."
        )

    if not result["special"]:
        recommendations.append(
            "Add special characters."
        )

    if result["common"]:
        recommendations.append(
            "Avoid common passwords."
        )

    if result["repeated"]:
        recommendations.append(
            "Avoid repeated characters."
        )

    if result["sequential"]:
        recommendations.append(
            "Avoid predictable sequences."
        )

    message = (
        "🔐 PASSWORD SECURITY REPORT\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "📊 SCORE\n"
        f"{result['score']} / 100\n\n"

        "🟢 STRENGTH\n"
        f"{result['strength']}\n\n"

        "📏 CHARACTERISTICS\n"
        f"Length: {result['length']}\n"
        f"Uppercase: "
        f"{'Yes ✅' if result['upper'] else 'No ❌'}\n"
        f"Lowercase: "
        f"{'Yes ✅' if result['lower'] else 'No ❌'}\n"
        f"Numbers: "
        f"{'Yes ✅' if result['digit'] else 'No ❌'}\n"
        f"Special characters: "
        f"{'Yes ✅' if result['special'] else 'No ❌'}\n\n"

        "🧠 SECURITY ANALYSIS\n"
        f"Estimated entropy: "
        f"{result['entropy']} bits\n"
        f"Common password: "
        f"{'Yes ⚠️' if result['common'] else 'No ✅'}\n"
        f"Repeated characters: "
        f"{'Yes ⚠️' if result['repeated'] else 'No ✅'}\n"
        f"Sequential pattern: "
        f"{'Yes ⚠️' if result['sequential'] else 'No ✅'}\n"
    )

    if recommendations:

        message += "\n💡 RECOMMENDATIONS\n"

        for recommendation in recommendations:
            message += f"• {recommendation}\n"

    else:

        message += (
            "\n✅ No basic weaknesses detected.\n"
        )

    message += (
        "\n━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔒 Password was not stored."
    )

    result_message = await update.message.reply_text(
        message
    )

    # Schedule deletion without blocking the bot
    context.job_queue.run_once(
        delete_password_result,
        60,
        data={
            "chat_id": update.effective_chat.id,
            "message_id": result_message.message_id
        }
    )
