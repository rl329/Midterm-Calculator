import os
import importlib
import pkgutil
from decimal import Decimal
from calculator_app.calculator import Calculator

def load_plugins():
    """Dynamically load plugins from the 'plugins' folder."""
    plugins = {}
    package = 'calculator_app.plugins'
    plugin_path = os.path.join(os.path.dirname(__file__), 'calculator_app', 'plugins')

    # Iterate through modules in the plugins directory
    for _, module_name, _ in pkgutil.iter_modules([plugin_path]):
        module = importlib.import_module(f"{package}.{module_name}")

        # Check for classes that end with 'Command'
        for attr in dir(module):
            cls = getattr(module, attr)
            if isinstance(cls, type) and cls.__name__.endswith('Command'):
                plugins[module_name] = cls

    return plugins

def show_initial_menu():
    """Display the initial prompt for user input."""
    print("Enter a command:")
    print("- menu (to display available commands)")
    print("- quit (to exit the program)")

def show_menu(available_commands):
    """Display the list of available commands."""
    print("\nAvailable commands:")
    for command in available_commands:
        print(f"- {command.replace('_command', '')}")
    print("- quit (to exit the program)")

def run_command(command_cls, calculator, a, b):
    """Execute a command with the provided inputs."""
    result = command_cls(calculator, a, b).execute()
    print(f"The result of {command_cls.__name__.replace('Command', '')} is: {result}")

def repl():
    """Run the REPL (Read-Eval-Print Loop) interface."""
    calculator = Calculator()
    commands = load_plugins()

    show_initial_menu()

    while True:
        user_input = input("Enter Command: ").strip().lower()

        if user_input == "quit":
            print("Exiting the program.")
            break
        elif user_input == "menu":
            show_menu(commands.keys())
            continue

        try:
            a = Decimal(input("Enter the first number: "))
            b = Decimal(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        command_key = f"{user_input}_command"
        if command_key in commands:
            command_cls = commands[command_key]
            run_command(command_cls, calculator, a, b)
        else:
            print("Invalid command!")

if __name__ == "__main__":
    repl()
