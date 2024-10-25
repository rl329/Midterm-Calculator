"""
This module contains tests for the Calculator class.
"""

from decimal import Decimal  # Move import to top-level
import pytest  # Move import to top-level
from calculator_app.calculator import Calculator

def test_addition():
    """Test that the addition function returns the correct result."""
    assert Calculator.add(Decimal(4), Decimal(3)) == Decimal(7)

def test_subtraction():
    """Test that the subtraction function returns the correct result."""
    assert Calculator.subtract(Decimal(4), Decimal(3)) == Decimal(1)

def test_multiplication():
    """Test that the multiplication function returns the correct result."""
    assert Calculator.multiply(Decimal(2), Decimal(2)) == Decimal(4)

def test_division():
    """Test that the division function returns the correct result."""
    assert Calculator.divide(Decimal(2), Decimal(2)) == Decimal(1)

def test_divide_by_zero():
    """Test division by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal('5'), Decimal('0'))
