from typing import List
from calculator_app.calculation import Calculation

class CalcHistory:
    """Manages a history of calculations."""

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Return the history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Return the latest calculation or None if history is empty."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
