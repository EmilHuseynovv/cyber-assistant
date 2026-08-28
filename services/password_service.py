import math
import re


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou",
}


def calculate_entropy(password: str) -> float:
    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"[0-9]", password):
        charset_size += 10

    if re.search(r"[^a-zA-Z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        return 0.0

    return round(
        len(password) * math.log2(charset_size),
        1
    )


def has_repeated_characters(password: str) -> bool:
    return bool(
        re.search(r"(.)\1{2,}", password)
    )


def has_sequential_pattern(password: str) -> bool:
    sequences = [
        "123456",
        "234567",
        "345678",
        "456789",
        "abcdef",
        "bcdefg",
        "qwerty",
        "asdfgh",
    ]

    password_lower = password.lower()

    return any(
        sequence in password_lower
        for sequence in sequences
    )


def analyze_password(password: str) -> dict:
    length = len(password)

    has_upper = bool(
        re.search(r"[A-Z]", password)
    )

    has_lower = bool(
        re.search(r"[a-z]", password)
    )

    has_digit = bool(
        re.search(r"[0-9]", password)
    )

    has_special = bool(
        re.search(r"[^a-zA-Z0-9]", password)
    )

    common = password.lower() in COMMON_PASSWORDS

    repeated = has_repeated_characters(
        password
    )

    sequential = has_sequential_pattern(
        password
    )

    entropy = calculate_entropy(password)

    score = 0

    # Length
    if length >= 16:
        score += 30
    elif length >= 12:
        score += 25
    elif length >= 8:
        score += 15

    # Character diversity
    if has_upper:
        score += 15

    if has_lower:
        score += 15

    if has_digit:
        score += 15

    if has_special:
        score += 15

    # Entropy
    if entropy >= 60:
        score += 15
    elif entropy >= 40:
        score += 8

    # Weakness penalties
    if common:
        score -= 40

    if repeated:
        score -= 10

    if sequential:
        score -= 15

    score = max(
        0,
        min(score, 100)
    )

    # Strength classification
    if common or score < 30:
        strength = "VERY WEAK 🔴"

    elif score < 50:
        strength = "WEAK 🟠"

    elif score < 70:
        strength = "MEDIUM 🟡"

    elif score < 85:
        strength = "STRONG 🟢"

    else:
        strength = "VERY STRONG 🟢"

    return {
        "length": length,
        "upper": has_upper,
        "lower": has_lower,
        "digit": has_digit,
        "special": has_special,
        "common": common,
        "repeated": repeated,
        "sequential": sequential,
        "entropy": entropy,
        "score": score,
        "strength": strength,
    }
