from typing import List, Callable
from decimal import Decimal
from calculator_app.operations import add, subtract, multiply, divide
from calculator_app.calculation import Calculation

class Calculator:
    """Calculator class to perform operations and manage calculations."""

    history: List[Calculation] = []

    operations_map = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    @classmethod
    def perform_operation(cls, a: Decimal, b: Decimal, operation_name: str) -> Decimal:
        """Perform the specified operation and store the result."""
        try:
            operation_func = cls.operations_map[operation_name]
        except KeyError:
            raise ValueError(f"Invalid operation: {operation_name}")

        result = operation_func(a, b)

        # Store the calculation in history
        calculation = Calculation.create(a, b, operation_func)
        cls.history.append(calculation)

        return result

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Return the history of all calculations."""
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest_calculation(cls) -> Calculation:
        """Retrieve the latest calculation from the history."""
        return cls.history[-1] if cls.history else None
