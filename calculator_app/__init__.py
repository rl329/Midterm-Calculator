"""
Calculator app package initialization.
"""

from calculator_app.calculations import Calculations
from calculator_app.operations import add, subtract, multiply, divide
from calculator_app.calculation import Calculation
from decimal import Decimal
from typing import Callable

class Calculator:
    """Calculator class to perform operations and manage calculations."""

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Perform addition."""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction."""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication."""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Perform division."""
        return Calculator._perform_operation(a, b, divide)
