from calculator_app.calculator import Calculator
from decimal import Decimal

def show_initial_menu():
    """Display the initial menu to the user."""
    print("Options:")
    print("menu - Display available commands")
    print("quit - Exit the program")

def show_menu():
    """Display available calculator operations."""
    print("\nAvailable commands:")
    print("- add")
    print("- subtract")
    print("- multiply")
    print("- divide")
    print("- quit (to exit the program)")

def run_command(command, calculator, a, b):
    """Execute the selected calculator command."""
    operations = {
        "add": calculator.add,
        "subtract": calculator.subtract,
        "multiply": calculator.multiply,
        "divide": calculator.divide,
    }

    if command in operations:
        try:
            result = operations[command](a, b)
            print(f"The result of {command} is: {result}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid command!")

def repl():
    """Run the calculator REPL (Read-Eval-Print Loop)."""
    calculator = Calculator()
    show_initial_menu()

    while True:
        user_input = input("Enter Command (Menu or Quit): ").strip().lower()

        if user_input == "quit":
            print("Exiting the program. Goodbye!")
            break
        elif user_input == "menu":
            show_menu()
            continue

        try:
            a = Decimal(input("Enter the first number: "))
            b = Decimal(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        run_command(user_input, calculator, a, b)

if __name__ == "__main__":
    repl()
