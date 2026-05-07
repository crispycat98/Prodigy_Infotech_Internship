import re
import getpass

CRITERIA = [
    ("length",    "At least 8 characters",          lambda p: len(p) >= 8),
    ("upper",     "Uppercase letter (A-Z)",          lambda p: bool(re.search(r"[A-Z]", p))),
    ("lower",     "Lowercase letter (a-z)",          lambda p: bool(re.search(r"[a-z]", p))),
    ("digit",     "Number (0-9)",                    lambda p: bool(re.search(r"\d", p))),
    ("special",   "Special character (!@#$...)",     lambda p: bool(re.search(r"[^a-zA-Z0-9]", p))),
    ("length16",  "16+ characters (bonus)",          lambda p: len(p) >= 16),
]

STRENGTH_LABELS = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]


def assess(password):
    results = {key: check(password) for key, _, check in CRITERIA}
    score = sum(results.values())
    label = STRENGTH_LABELS[min(score, len(STRENGTH_LABELS) - 1)]
    return score, label, results


def display_report(password):
    score, label, results = assess(password)

    print(f"\n  Strength : {label} ({score}/{len(CRITERIA)})")
    print("  Criteria :")
    for key, desc, _ in CRITERIA:
        status = "✔" if results[key] else "✘"
        print(f"    [{status}] {desc}")

    tips = [desc for key, desc, _ in CRITERIA if not results[key]]
    if tips:
        print("\n  To improve, add:")
        for tip in tips:
            print(f"    → {tip}")
    print()


def main():
    print("=" * 42)
    print("       Password Complexity Checker")
    print("=" * 42)

    while True:
        password = getpass.getpass("\nEnter password (hidden): ")
        if not password:
            print("No input received. Exiting.")
            break

        display_report(password)

        again = input("Check another? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
