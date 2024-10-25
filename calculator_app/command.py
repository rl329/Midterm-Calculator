"""
Command classes for calculator operations and the menu command.
"""

from decimal import Decimal
from calculator_app.calculator import Calculator

class Command:
    """Abstract command class."""
    def __init__(self, calculator: Calculator, a: Decimal = None, b: Decimal = None):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        """Execute the command."""
        raise NotImplementedError("Execute method not implemented.")

class AddCommand(Command):
    """Command to perform addition."""
    def execute(self) -> Decimal:
        return self.calculator.add(self.a, self.b)

class SubtractCommand(Command):
    """Command to perform subtraction."""
    def execute(self) -> Decimal:
        return self.calculator.subtract(self.a, self.b)

class MultiplyCommand(Command):
    """Command to perform multiplication."""
    def execute(self) -> Decimal:
        return self.calculator.multiply(self.a, self.b)

class DivideCommand(Command):
    """Command to perform division."""
    def execute(self) -> Decimal:
        return self.calculator.divide(self.a, self.b)

class MenuCommand(Command):
    """Command to display the menu."""
    def __init__(self, available_commands):
        self.available_commands = available_commands

    def execute(self):
        """Display the menu of available commands."""
        print("\nAvailable commands:")
        for command in self.available_commands:
            print(f"- {command}")
        print("- quit (to exit the program)")
