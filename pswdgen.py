# Password generator utility
import random
import time

# Allowed characters for password generation
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

def create_password(length):
    """Generates a random password of given length."""
    return "".join(random.choice(CHARACTERS) for _ in range(length))

def run_pswdgen():
    """Runs the interactive password generator."""
    print("\n🔐 Password Generator\n")
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("⚠️ Length must be a positive number!")
            return
        password = create_password(length)
        print(f"\n✅ Your password: {password}")
    except ValueError:
        print("❌ Error: please enter a valid number.")
    time.sleep(2)
    input("\nPress Enter to return to menu...")
