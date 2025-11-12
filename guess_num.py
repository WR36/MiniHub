import random

def randomizer():
    """Number guessing game."""
    secret_number = random.randint(1, 10)
    attempts = 0
    print("\n🎯 Guess the Number (1–10)\n")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if guess == secret_number:
            print(f"🎉 You guessed the number in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("⬆️ The secret number is higher.")
        else:
            print("⬇️ The secret number is lower.")

def run_randomizer():
    """Starts the guessing game."""
    randomizer()
    input("\nPress Enter to return to the menu...")