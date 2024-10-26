import pandas as pd
from typing import List
from decimal import Decimal
from calculator_app.calculation import Calculation

class CalcHistory:
    """Class to manage the history of calculations."""
    _history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls._history.append(calculation)

    @classmethod
    def clear_history(cls):
        """Clear the entire history."""
        cls._history.clear()

    @classmethod
    def get_history(cls) -> pd.DataFrame:
        """Return the history as a Pandas DataFrame."""
        data = [
            (calc.a, calc.b, calc.operation_name, calc.perform())
            for calc in cls._history
        ]
        return pd.DataFrame(data, columns=["A", "B", "Operation", "Result"])

    @classmethod
    def get_latest(cls) -> Calculation:
        """Retrieve the latest calculation from history."""
        if not cls._history:
            raise ValueError("No calculations in history.")
        return cls._history[-1]

    @classmethod
    def save_history(cls, filename: str = "history.csv"):
        """Save the history to a CSV file."""
        df = cls.get_history()
        df.to_csv(filename, index=False)
        print(f"History saved to {filename}.")

    @classmethod
    def load_history(cls, filename: str = "history.csv") -> None:
        """Load the history from a CSV file."""
        try:
            # Handle the case where the file exists but has no columns or rows
            df = pd.read_csv(filename)
            if df.empty or df.shape[1] == 0:
                print("The history file is empty or invalid.")
                cls._history = []  # Ensure history is cleared
                return

            # Reconstruct Calculation objects from valid rows
            cls._history = [
                Calculation(
                    Decimal(row["A"]),
                    Decimal(row["B"]),
                    row["Operation"],
                    Decimal(row["Result"])
                )
                for _, row in df.iterrows()
            ]
            print(f"History loaded from {filename}.")

        except pd.errors.EmptyDataError:
            print(f"{filename} is empty. No history loaded.")
            cls._history = []  # Clear history for empty file
            return

        except FileNotFoundError:
            print(f"{filename} not found.")
            raise  # Re-raise the exception for tests to catch

        except Exception as e:
            print(f"Error loading history: {e}")
