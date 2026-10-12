import hashlib
import re
from pathlib import Path

PASSWORD_FILE = Path(__file__).with_name("common_passwords.txt")


def generate_hash(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def load_common_passwords(filename=PASSWORD_FILE):
    path = Path(filename)
    if not path.exists():
        return set()

    with path.open("r", encoding="utf-8") as file:
        return {line.strip().lower() for line in file if line.strip()}


def check_common_password(password, common_passwords):
    return password.lower() in common_passwords


def basic_strength_check(password):
    checks = [
        (len(password) >= 8, "Use at least 8 characters."),
        (bool(re.search(r"[A-Z]", password)), "Add an uppercase letter."),
        (bool(re.search(r"[a-z]", password)), "Add a lowercase letter."),
        (bool(re.search(r"[0-9]", password)), "Add a number."),
        (bool(re.search(r"[^A-Za-z0-9]", password)), "Add a special character."),
    ]

    score = sum(passed for passed, _ in checks)
    suggestions = [message for passed, message in checks if not passed]
    return score, suggestions


def analyze_module2(password):
    common_passwords = load_common_passwords()
    score, suggestions = basic_strength_check(password)

    return {
        "hash": generate_hash(password),
        "common": check_common_password(password, common_passwords),
        "score": score,
        "suggestions": suggestions,
    }


if __name__ == "__main__":
    print("PASSWORD STRENGTH ANALYZER - MODULE 2")
    password = input("Enter password: ")
    result = analyze_module2(password)
    print("\nSHA-256 Hash:", result["hash"])
    print("Common Password:", "YES" if result["common"] else "NO")
    print("Score:", result["score"], "/ 5")
    if result["suggestions"]:
        print("Suggestions:")
        for suggestion in result["suggestions"]:
            print("-", suggestion)
