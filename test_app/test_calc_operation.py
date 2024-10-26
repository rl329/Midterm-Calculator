"""
This module contains calculator operations.
"""

# test_app/test_calc_operation.py

from decimal import Decimal
import pytest
from calculator_app.calc_operation import add, subtract, multiply, divide

def test_add_operation():
    """Test the addition operation."""
    assert add(Decimal('5'), Decimal('2')) == Decimal('7')

def test_subtract_operation():
    """Test the subtraction operation."""
    assert subtract(Decimal('9'), Decimal('2')) == Decimal('7')

def test_multiply_operation():
    """Test the multiplication operation."""
    assert multiply(Decimal('2'), Decimal('4')) == Decimal('8')

def test_divide_operation():
    """Test the division operation."""
    assert divide(Decimal('8'), Decimal('2')) == Decimal('4')

def test_divide_by_zero():
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(Decimal('7'), Decimal('0'))
