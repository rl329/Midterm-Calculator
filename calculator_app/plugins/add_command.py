from decimal import Decimal
from calculator_app.calculator import Calculator

class AddCommand:
    """Command to perform addition."""

    def __init__(self, calculator, a: Decimal, b: Decimal):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        """Execute the addition command."""
        return self.calculator.perform_operation(self.a, self.b, "add")
