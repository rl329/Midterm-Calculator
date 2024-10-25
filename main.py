from multiprocessing import Process
from decimal import Decimal
from calculator_app.calculator import Calculator
import importlib
import pkgutil
import os

def load_plugins():
    """
    Dynamically load all available plugins from the 'plugins' directory.
    """
    plugins = {}
    package = 'calculator_app.plugins'
    plugin_path = os.path.join(os.path.dirname(__file__), 'calculator_app', 'plugins')

    for _, module_name, _ in pkgutil.iter_modules([plugin_path]):
        module = importlib.import_module(f"{package}.{module_name}")

        for attr in dir(module):
            cls = getattr(module, attr)
            if isinstance(cls, type) and cls.__name__.endswith('Command'):
                plugins[module_name] = cls

    return plugins

def show_initial_menu():
    """
    Display the initial menu with options.
    """
    print("Enter a command:")
    print("Options: 'menu', 'quit'")

def show_menu(available_commands):
    """
    Display all available commands from plugins.
    """
    print("\nAvailable commands:")
    for command in available_commands:
        print(f"- {command.replace('_command', '')}")
    print("- quit (to exit the program)")

def run_command_in_process(command_cls, calculator, a, b):
    """
    Run a command in a separate process.
    """
    process = Process(target=execute_command, args=(command_cls, calculator, a, b))
    process.start()
    process.join()

def execute_command(command_cls, calculator, a, b):
    """
    Execute the given command.
    """
    command = command_cls(calculator, a, b)
    result = command.execute()
    print(f"The result is: {result}")

def repl():
    """
    Start the REPL loop to interact with the calculator.
    """
    calculator = Calculator()
    commands = load_plugins()

    show_initial_menu()

    while True:
        user_input = input("\nEnter Command (menu or quit): ").strip().lower()

        if user_input == "quit":
            print("Exiting...")
            break
        elif user_input == "menu":
            show_menu(commands.keys())
            continue

        if f"{user_input}_command" in commands:
            command_cls = commands[f"{user_input}_command"]
            try:
                a = Decimal(input("Enter the first number: "))
                b = Decimal(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            # Run command in a separate process
            run_command_in_process(command_cls, calculator, a, b)
        else:
            print("Invalid command!")

if __name__ == "__main__":
    repl()
