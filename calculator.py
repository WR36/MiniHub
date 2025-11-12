def calc(op, num1, num2):
    """Performs a simple arithmetic operation."""
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2
    else:
        raise ValueError("Invalid operator")

def run_calc():
    """Runs the calculator interaction loop."""
    print("\n📘 Calculator launched\n")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Operator (+, -, /, *): ")
        num2 = float(input("Enter second number: "))
        print(f"💡 Result: {calc(op, num1, num2)}")
    except ZeroDivisionError:
        print("❌ Division by zero!")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    input("\nPress Enter to return to the menu...")