def truncate_text(text: str, limit: int = 3500) -> str:
    if len(text) <= limit:
        return text

    return text[:limit] + "\n\n...output truncated."


def format_section(title: str, content: str) -> str:
    return (
        f"{title}\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"{content}\n"
    )
