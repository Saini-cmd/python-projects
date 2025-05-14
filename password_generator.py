import random
import string

def main():
    print("Welcome to the Random Password Generator!")
    print("=========================================")
    
    try:
        password_length = int(input("How long would you like your password to be? (Enter a number): "))
        
        if password_length <= 0:
            print("Oops! The password length must be a positive number.")
            return
        elif password_length < 6:
            print("Hmm... Short passwords aren't very secure. Consider making it longer.")
        elif password_length > 50:
            print("Long passwords can be a bit tricky to remember, but totally secure!")
            
    except ValueError:
        print("Uh-oh! Please enter a valid number for the password length.")
        return
    
    print("\nNow, let's customize your password. You can choose what characters to include:")
    
    include_lowercase = input("Include lowercase letters (a-z)? (yes/no): ").strip().lower() == 'yes'
    include_uppercase = input("Include uppercase letters (A-Z)? (yes/no): ").strip().lower() == 'yes'
    include_numbers = input("Include numbers (0-9)? (yes/no): ").strip().lower() == 'yes'
    include_symbols = input("Include special symbols (!, @, #, $, etc.)? (yes/no): ").strip().lower() == 'yes'
    
    if not (include_lowercase or include_uppercase or include_numbers or include_symbols):
        print("Oops! You need to select at least one character type to proceed.")
        return
    
    char_pool = ""
    if include_lowercase:
        char_pool += string.ascii_lowercase
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_numbers:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation
    
    try:
        # Randomly generate the password based on user preferences
        password = "".join(random.choice(char_pool) for _ in range(password_length))
        
        print("\nHere's your generated password:")
        print(password)
        
        # Assess the strength of the password based on length and character variety
        strength = "Weak"
        if password_length >= 8 and (include_lowercase + include_uppercase + include_numbers + include_symbols) >= 3:
            strength = "Strong"
        elif password_length >= 6 and (include_lowercase + include_uppercase + include_numbers + include_symbols) >= 2:
            strength = "Medium"
        
        print(f"Password strength: {strength}")
        
    except Exception as e:
        print(f"Something went wrong while generating the password: {e}")

if __name__ == "__main__":
    main()
