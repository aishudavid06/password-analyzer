import re
import random
import string

common_passwords = ["123456", "password", "qwerty", "abc123", "111111"]

def is_unique(password):
    patterns = ["123", "abc", "qwerty"]
    for p in patterns:
        if p in password.lower():
            return False
    return True


def check_password_strength(password):

    # Minimum length rule
    if len(password) < 8:
        return "Password must be at least 8 characters ❌"

    score = 0

    # Length scoring
    if len(password) >= 12:
        score += 2
    else:
        score += 1

    # Complexity checks
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    # Common password check
    if password.lower() in common_passwords:
        return "Very Weak ❌"

    # Uniqueness check
    if not is_unique(password):
        return "Weak (Pattern Detected) ⚠️"

    # Final strength
    if score <= 2:
        return "Weak 🔴"
    elif score <= 4:
        return "Medium 🟡"
    else:
        return "Strong 🟢"


def suggest_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))