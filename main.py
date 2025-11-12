import os
import time
import calculator
import pswdgen
import guess_num

# Clears the console screen depending on OS
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Main menu loop
def main():
    while True:
        clear_screen()
        print("╔══════════════════════╗")
        print("║      MiniHub v1.0    ║")
        print("╠══════════════════════╣")
        print("║ 1. Calculator        ║")
        print("║ 2. Password Generator║")
        print("║ 3. Guess the Number  ║")
        print("║ 0. Exit              ║")
        print("╚══════════════════════╝")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("❌ Please enter a number between 0 and 3!")
            time.sleep(2)
            continue

        # Menu options
        if choice == 1:
            calculator.run_calc()
        elif choice == 2:
            pswdgen.run_pswdgen()
        elif choice == 3:
            guess_num.run_randomizer()
        elif choice == 0:
            print("\n👋 Program terminated by user.")
            break
        else:
            print("⚠️ Invalid choice.")
            time.sleep(2)

# Program entry point
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🚪 Program closed manually.")
