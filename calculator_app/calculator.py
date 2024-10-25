from typing import List, Callable
from calculator_app.calc_operation import add, subtract, multiply, divide
from calculator_app.calculation import Calculation
from decimal import Decimal

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
        """Perform a mathematical operation and store the result."""
        try:
            operation_func = cls.operations_map[operation_name]
        except KeyError:
            raise ValueError(f"Invalid operation: {operation_name}")

        result = operation_func(a, b)
        calculation = Calculation(a, b, operation_func)
        cls.history.append(calculation)
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Perform addition."""
        return Calculator.perform_operation(a, b, "add")

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction."""
        return Calculator.perform_operation(a, b, "subtract")

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication."""
        return Calculator.perform_operation(a, b, "multiply")

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Perform division."""
        if b == Decimal("0"):
            raise ZeroDivisionError("Cannot divide by zero.")
        return Calculator.perform_operation(a, b, "divide")

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Get the history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        """Clear the calculation history."""
        cls.history.clear()

    @classmethod
    def get_latest_calculation(cls) -> Calculation:
        """Get the latest calculation from history."""
        return cls.history[-1] if cls.history else None
