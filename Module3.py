import re
from Module2 import analyze_module2


def check_repeated_characters(password):
    return bool(re.search(r"(.)\1\1", password))


def check_sequential_pattern(password):
    password = password.lower()

    for i in range(len(password) - 3):
        part = password[i:i + 4]

        if all(ord(part[j + 1]) - ord(part[j]) == 1 for j in range(3)):
            return True

        if all(ord(part[j]) - ord(part[j + 1]) == 1 for j in range(3)):
            return True

    return False


def check_same_character(password):
    if not password:
        return False

    most_common_count = max(password.count(character) for character in set(password))
    return most_common_count >= len(password) * 0.6


def advanced_analysis(password):
    warnings = []

    if check_repeated_characters(password):
        warnings.append("Avoid repeated characters.")

    if check_sequential_pattern(password):
        warnings.append("Avoid sequential patterns like 1234 or abcd.")

    if check_same_character(password):
        warnings.append("Avoid using the same character too frequently.")

    return warnings


def analyze_module3(password):
    result = analyze_module2(password)
    result["advanced_warnings"] = advanced_analysis(password)
    return result


if __name__ == "__main__":
    print("PASSWORD STRENGTH ANALYZER - MODULE 3")
    password = input("Enter password: ")
    result = analyze_module3(password)

    print("\nSHA-256 Hash:", result["hash"])
    print("Common Password:", "YES" if result["common"] else "NO")
    print("Basic Score:", result["score"], "/ 5")
    print("\nAdvanced Analysis:")

    if result["advanced_warnings"]:
        for warning in result["advanced_warnings"]:
            print("-", warning)
    else:
        print("No major patterns detected.")
