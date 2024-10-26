"""
This module contains tests for the Calculator class.
"""

import os
from decimal import Decimal
import pytest
from calculator_app.calculator import Calculator

def test_save_history(tmp_path):
    """Test that history is saved correctly to a CSV."""
    Calculator.history.clear()
    Calculator.perform_operation(Decimal(1), Decimal(2), "add")
    filepath = tmp_path / "test_history.csv"

    Calculator.save_history(str(filepath))
    assert os.path.exists(filepath)  # Check if the file was created

def test_load_history(tmp_path):
    """Test loading history from a CSV file."""
    # Create a CSV with history data
    filepath = tmp_path / "test_history.csv"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("A,B,Operation,Result\n1,2,add,3\n3,1,subtract,2\n")

    Calculator.load_history(str(filepath))
    assert len(Calculator.history) == 2  # Ensure history is loaded
    assert Calculator.history[0].result == Decimal(3)
    assert Calculator.history[1].operation_name == "subtract"

def test_load_history_file_not_found():
    """Test loading history when the CSV file is not found."""
    filename = "non_existent_file.csv"

    # Ensure the file does not exist before the test
    if os.path.exists(filename):
        os.remove(filename)

    with pytest.raises(FileNotFoundError):
        Calculator.load_history(filename)

def test_zero_and_negative_division():
    """Test operations with zero and negative numbers."""
    assert Calculator.perform_operation(Decimal(0), Decimal(10), "add") == Decimal(10)
    assert Calculator.perform_operation(Decimal(-1), Decimal(-5), "multiply") == Decimal(5)

def test_average_result_in_summary(capsys):
    """Test that the summary calculates the average result correctly."""
    Calculator.history.clear()
    Calculator.perform_operation(Decimal(3), Decimal(3), "add")  # Result = 6
    Calculator.perform_operation(Decimal(10), Decimal(2), "subtract")  # Result = 8

    Calculator.summarize_history()
    captured = capsys.readouterr().out

    print(f"Captured Output:\n{captured}")  # For debugging

    assert "Average result: 7" in captured

def test_filter_history_empty():
    """Test filtering history when no matching operations are found."""
    Calculator.history.clear()
    Calculator.perform_operation(Decimal(3), Decimal(3), "add")

    filtered_df = Calculator.filter_history("divide")
    assert filtered_df.empty  # No divide operations, so should be empty
