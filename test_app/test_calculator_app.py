"""Tests for the Calculator class."""

# pylint: disable=redefined-outer-name
import pytest
from calculator_app.calculator import Calculator

@pytest.fixture
def setup_calculator():
    """Fixture to clear calculator history before each test."""
    Calculator.clear_history()
    yield

def test_addition(setup_calculator):
    """Test the addition method."""
    assert Calculator.add(2, 3) == 5

def test_subtraction(setup_calculator):
    """Test the subtraction method."""
    assert Calculator.subtract(5, 2) == 3

def test_multiplication(setup_calculator):
    """Test the multiplication method."""
    assert Calculator.multiply(3, 4) == 12

def test_division(setup_calculator):
    """Test the division method."""
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero_exception(setup_calculator):
    """Test that division by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

def test_last_result(setup_calculator):
    """Test retrieving the last result from history."""
    Calculator.add(1, 1)
    assert Calculator.get_last_result() == 2

def test_clear_history(setup_calculator):
    """Test clearing the calculator history."""
    Calculator.add(2, 2)
    Calculator.clear_history()
    with pytest.raises(ValueError):
        Calculator.get_last_result()
