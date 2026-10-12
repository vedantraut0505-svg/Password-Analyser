# from getpass import getpass
from Module3 import analyze_module3


def calculate_strength(result):
    if result["common"]:
        return "WEAK"

    score = result["score"]
    warnings = result["advanced_warnings"]

    if score <= 2:
        return "WEAK"
    if score <= 4:
        return "MEDIUM"
    if warnings:
        return "MEDIUM"

    return "STRONG"


def generate_suggestions(result):
    suggestions = list(result["suggestions"])

    for warning in result["advanced_warnings"]:
        if warning not in suggestions:
            suggestions.append(warning)

    if result["common"]:
        suggestions.append("Avoid using a commonly used password.")

    return suggestions


def complete_analysis(password):
    result = analyze_module3(password)
    result["strength"] = calculate_strength(result)
    result["final_suggestions"] = generate_suggestions(result)
    return result


def display_result(result):
    print("\n" + "=" * 55)
    print("          PASSWORD ANALYSIS RESULT")
    print("=" * 55)
    print("Common Password :", "YES" if result["common"] else "NO")
    print("Basic Score     :", f'{result["score"]}/5')
    print("Final Strength  :", result["strength"])
    print("\nSHA-256 Hash:")
    print(result["hash"])

    if result["advanced_warnings"]:
        print("\nAdvanced Warnings:")
        for warning in result["advanced_warnings"]:
            print("-", warning)

    if result["final_suggestions"]:
        print("\nSuggestions:")
        for suggestion in result["final_suggestions"]:
            print("-", suggestion)
    else:
        print("\nSuggestions: No basic improvements detected.")

    print("=" * 55)


def main():
    print("=" * 55)
    print("       PASSWORD STRENGTH ANALYZER")
    print("              USING HASHING")
    print("=" * 55)

    password = input("\nSet your password: ")
    if not password:
        print("Password cannot be empty.")
        return

    display_result(complete_analysis(password))


if __name__ == "__main__":
    main()
