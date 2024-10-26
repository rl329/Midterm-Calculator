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
    def execute(self) -> Decimal:
        """Execute the addition command."""
        return self.calculator.perform_operation(self.a, self.b, "add")

class SubtractCommand(Command):
    def execute(self) -> Decimal:
        """Execute the subtraction command."""
        return self.calculator.perform_operation(self.a, self.b, "subtract")

class MultiplyCommand(Command):
    def execute(self) -> Decimal:
        """Execute the multiplication command."""
        return self.calculator.perform_operation(self.a, self.b, "multiply")

class DivideCommand(Command):
    def execute(self) -> Decimal:
        """Execute the division command."""
        return self.calculator.perform_operation(self.a, self.b, "divide")


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
