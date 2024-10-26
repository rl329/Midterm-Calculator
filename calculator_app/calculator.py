import pandas as pd
from typing import List, Callable
from calculator_app.calc_operation import add, subtract, multiply, divide
from calculator_app.calculation import Calculation
from decimal import Decimal
import os  # Import 'os' to check for file existence

class Calculator:
    """Calculator class to perform operations and manage calculations."""

    history: List[Calculation] = []  # Store Calculation objects in memory

    operations_map = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: a / b if b != 0 else Decimal("Infinity"),
    }

    @classmethod
    def perform_operation(cls, a: Decimal, b: Decimal, operation_name: str) -> Decimal:
        """Perform a mathematical operation and store the result."""
        if operation_name not in cls.operations_map:
            raise ValueError(f"Invalid operation: {operation_name}")

        operation_func = cls.operations_map[operation_name]
        result = operation_func(a, b)

        if operation_name == "divide" and b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        # Create and store the Calculation object
        calculation = Calculation.create(a, b, operation_func, operation_name)
        cls.history.append(calculation)
        print(f"Added to history: {calculation}")

        return result

    @classmethod
    def get_history_as_dataframe(cls) -> pd.DataFrame:
        """Return the history as a Pandas DataFrame."""
        if not cls.history:
            print("History is empty.")
            return pd.DataFrame(columns=["A", "B", "Operation", "Result"])

        data = [
            (c.a, c.b, c.operation_name, c.result) for c in cls.history
        ]
        return pd.DataFrame(data, columns=["A", "B", "Operation", "Result"])

    @classmethod
    def save_history(cls, filename: str = "history.csv"):
        """Save history to a CSV file using Pandas."""
        df = cls.get_history_as_dataframe()
        df.to_csv(filename, index=False)
        print(f"History saved to {filename}.")

    @classmethod
    def load_history(cls, filename: str = "history.csv"):
        """Load history from a CSV file using Pandas."""
        # Check if the file exists before attempting to read
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"{filename} not found.")

        try:
            df = pd.read_csv(filename)
            if df.empty:
                print("CSV file is empty. No history loaded.")
                return

            cls.history = [
                Calculation(
                    Decimal(row["A"]),
                    Decimal(row["B"]),
                    row["Operation"],
                    Decimal(row["Result"]),
                )
                for _, row in df.iterrows()
            ]
            print(f"History loaded from {filename}.")
        except Exception as e:
            print(f"Error loading history: {e}")

    @classmethod
    def summarize_history(cls):
        """Provide a summary of the history using Pandas."""
        df = cls.get_history_as_dataframe()
        if df.empty:
            print("No history available to summarize.")
            return

        print("\nHistory Summary:")
        print(f"Total calculations: {len(df)}")
        print(df["Operation"].value_counts())
        print(f"Average result: {df['Result'].mean()}")

    @classmethod
    def filter_history(cls, operation_name: str) -> pd.DataFrame:
        """Filter history to show only specific operations."""
        df = cls.get_history_as_dataframe()
        filtered_df = df[df["Operation"] == operation_name]
        print(f"\nFiltered History (Operation = {operation_name}):")
        print(filtered_df)
        return filtered_df
