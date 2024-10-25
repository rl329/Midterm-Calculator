"""Calculator module containing arithmetic operations and history management."""

from typing import List, Tuple, Union

class Calculator:
    """A class that performs basic arithmetic operations with history tracking."""

    history: List[Tuple[str, Union[int, float]]] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        Calculator.history.append(("add", result))
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract two numbers."""
        result = a - b
        Calculator.history.append(("subtract", result))
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        Calculator.history.append(("multiply", result))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide two numbers. Raises an exception if dividing by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculator.history.append(("divide", result))
        return result

    @classmethod
    def get_last_result(cls) -> Union[int, float]:
        """Retrieve the result of the last calculation."""
        if cls.history:
            return cls.history[-1][1]
        raise ValueError("No calculations in history.")

    @classmethod
    def clear_history(cls) -> None:
        """Clear the calculation history."""
        cls.history.clear()
