import os
import logging
from multiprocessing import Process
from decimal import Decimal
from calculator_app.calculator import Calculator
import importlib
import pkgutil
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set up logging configuration
logging.basicConfig(
    filename='app.log',  # Save logs to 'app.log'
    filemode='a',  # Append mode
    level=logging.INFO,  # Set logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log environment info and also print them to console
env_name = os.getenv("ENV_NAME", "development")
api_key = os.getenv("API_KEY", "your_api_key_here")

env_message = f"Running in {env_name} mode"
api_message = f"Using API key: {api_key}"

# Log both environment mode and API key
logging.info(env_message)
logging.info(api_message)

# Optionally print both to the console
print(env_message)
print(api_message)

def load_plugins():
    plugins = {}
    package = 'calculator_app.plugins'
    plugin_path = os.path.join(os.path.dirname(__file__), 'calculator_app', 'plugins')

    for _, module_name, _ in pkgutil.iter_modules([plugin_path]):
        module = importlib.import_module(f"{package}.{module_name}")

        for attr in dir(module):
            cls = getattr(module, attr)
            if isinstance(cls, type) and cls.__name__.endswith('Command'):
                plugins[module_name] = cls

    logging.info(f"Loaded plugins: {list(plugins.keys())}")
    return plugins

def show_initial_menu():
    logging.info("Displaying initial menu")
    print("\nEnter a command:")
    print("Options: 'menu', 'quit'")

def show_menu(available_commands):
    print("\nAvailable commands:")
    for command in available_commands:
        print(f"- {command.replace('_command', '')}")
    print("- quit (to exit the program)")

def run_command_in_process(command_cls, calculator, a, b):
    process = Process(target=execute_command, args=(command_cls, calculator, a, b))
    process.start()
    process.join()

def execute_command(command_cls, calculator, a, b):
    command = command_cls(calculator, a, b)
    result = command.execute()
    logging.info(f"Executed command: {command_cls.__name__} with inputs {a}, {b}")
    print(f"The result is: {result}")

def repl():
    calculator = Calculator()
    commands = load_plugins()

    show_initial_menu()

    while True:
        user_input = input("\nEnter Command (menu or quit): ").strip().lower()

        if user_input == "quit":
            logging.info("User exited the program")
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
                logging.error("Invalid input. Please enter numeric values.")
                print("Invalid input. Please enter numeric values.")
                continue

            run_command_in_process(command_cls, calculator, a, b)
        else:
            logging.warning(f"Invalid command entered: {user_input}")
            print("Invalid command!")

if __name__ == "__main__":
    repl()
