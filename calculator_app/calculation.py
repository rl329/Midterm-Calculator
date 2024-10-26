from decimal import Decimal
from typing import Callable

class Calculation:
    """Represents a mathematical calculation with two operands and an operation."""

    def __init__(self, a: Decimal, b: Decimal, operation_name: str, result: Decimal):
        self.a = a
        self.b = b
        self.operation_name = operation_name
        self.result = result

    @staticmethod
    def create(
        a: Decimal, b: Decimal, operation_func: Callable[[Decimal, Decimal], Decimal], operation_name: str
    ) -> 'Calculation':
        """Factory method to create a new calculation."""
        result = operation_func(a, b)
        return Calculation(a, b, operation_name, result)

    def perform(self) -> Decimal:
        """Return the result of the calculation."""
        return self.result

    def __repr__(self) -> str:
        """Return a string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, '{self.operation_name}', {self.result})"
