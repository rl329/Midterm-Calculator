"""
This module contains calculator history tests.
"""

from decimal import Decimal
import pytest
from calculator_app.calc_history import CalcHistory
from calculator_app.calculation import Calculation
from calculator_app.calc_operation import add, subtract, multiply

@pytest.fixture(autouse=True)
def setup_history():
    """Setup fixture to clear history and add sample calculations."""
    CalcHistory.clear_history()
    CalcHistory.add_calculation(
        Calculation.create(Decimal('3'), Decimal('2'), add, 'add')
    )

def test_add_calculation():
    """Test adding a calculation to the history."""
    calc = Calculation.create(Decimal('4'), Decimal('2'), add, 'add')
    CalcHistory.add_calculation(calc)
    assert CalcHistory.get_latest() == calc

def test_clear_history():
    """Test clearing the entire history."""
    CalcHistory.clear_history()
    assert len(CalcHistory.get_history()) == 0

def test_get_latest():
    """Test retrieving the latest calculation from the history."""
    latest = CalcHistory.get_latest()
    assert latest.a == Decimal('3') and latest.b == Decimal('2')

def test_save_and_load_history():
    """Test saving and loading the history."""
    CalcHistory.clear_history()
    calc = Calculation.create(Decimal('2'), Decimal('3'), add, 'add')
    CalcHistory.add_calculation(calc)

    CalcHistory.save_history("test_history.csv")
    CalcHistory.clear_history()
    CalcHistory.load_history("test_history.csv")

    loaded_history = CalcHistory.get_history()
    assert len(loaded_history) == 1
    assert loaded_history.iloc[0]['Operation'] == 'add'

def test_load_history_file_not_found():
    """Test loading history when the file is missing."""
    with pytest.raises(FileNotFoundError):
        CalcHistory.load_history("nonexistent_file.csv")

def test_load_empty_file():
    """Test loading an empty CSV file."""
    with open("empty_history.csv", "w", encoding="utf-8") as f:
        f.write("")  # Ensure the file is truly empty

    CalcHistory.load_history("empty_history.csv")
    assert len(CalcHistory.get_history()) == 0  # History should be empty

def test_add_multiple_operations():
    """Test adding multiple operations to the history."""
    CalcHistory.clear_history()
    calc1 = Calculation.create(Decimal('5'), Decimal('2'), subtract, 'subtract')
    calc2 = Calculation.create(Decimal('3'), Decimal('3'), multiply, 'multiply')
    CalcHistory.add_calculation(calc1)
    CalcHistory.add_calculation(calc2)

    history = CalcHistory.get_history()
    assert len(history) == 2
    assert history.iloc[0]['Operation'] == 'subtract'
    assert history.iloc[1]['Operation'] == 'multiply'
