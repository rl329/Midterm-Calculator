import logging
from decimal import Decimal
from calculator_app.calculator import Calculator

logging.basicConfig(filename="app.log", level=logging.INFO)

def show_menu():
    """Display the available commands."""
    print("\nOptions: 'menu', 'history', 'save', 'load', 'clear', 'summary', 'filter', 'quit'")
    print("- add")
    print("- subtract")
    print("- multiply")
    print("- divide")

def show_history():
    """Display the calculation history."""
    history_df = Calculator.get_history_as_dataframe()
    if history_df.empty:
        print("No history available.")
    else:
        print("\nCalculation History:")
        print(history_df)

def main():
    """Main program loop."""
    while True:
        user_input = input("\nEnter Command (menu, history, save, load, summary, filter, clear, quit): ").strip().lower()

        if user_input == "quit":
            print("Exiting...")
            break
        elif user_input == "menu":
            show_menu()
        elif user_input == "history":
            show_history()
        elif user_input == "save":
            Calculator.save_history()
        elif user_input == "load":
            Calculator.load_history()
        elif user_input == "summary":
            Calculator.summarize_history()
        elif user_input == "filter":
            operation = input("Enter operation to filter by (add, subtract, multiply, divide): ").strip().lower()
            Calculator.filter_history(operation)
        elif user_input == "clear":
            Calculator.clear_history()
        elif user_input in ["add", "subtract", "multiply", "divide"]:
            try:
                a = Decimal(input("Enter the first number: "))
                b = Decimal(input("Enter the second number: "))
                result = Calculator.perform_operation(a, b, user_input)
                print(f"The result is: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
