import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Criteria weights
    length_weight = 2
    uppercase_weight = 1
    lowercase_weight = 1
    number_weight = 1
    special_char_weight = 2

    # Length check
    if len(password) >= 12:
        strength += length_weight
    else:
        feedback.append("Password should be at least 12 characters long.")

    # Uppercase letter check
    if re.search(r'[A-Z]', password):
        strength += uppercase_weight
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase letter check
    if re.search(r'[a-z]', password):
        strength += lowercase_weight
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Number check
    if re.search(r'[0-9]', password):
        strength += number_weight
    else:
        feedback.append("Password should contain at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*()]', password):
        strength += special_char_weight
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*()).")

    # Determine strength level
    if strength >= 7:
        strength_level = "Strong"
    elif strength >= 4:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    return strength_level, feedback

def main():
    password = input("Enter your password: ")
    strength_level, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength_level}")
    if feedback:
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
