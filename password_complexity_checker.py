import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Strength Score Calculation
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    # Determine the strength level based on the score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Your password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Your password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Your password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Your password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Your password should contain at least one special character (e.g., !@#$%^&*).")
    
    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "_main_":
    main() 
