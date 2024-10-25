"""
This module contains tests for individual calculator operations.
"""

from decimal import Decimal
import pytest
from calculator_app.calculation import Calculation
from calculator_app.calc_operation import add, subtract, multiply, divide

def perform_and_check(num1, num2, operation, expected):
    """
    Helper function to create a calculation and verify the result.
    """
    calc = Calculation.create(num1, num2, operation)
    assert calc.perform() == expected

def test_add_operation():
    """
    Test the addition operation.
    """
    perform_and_check(Decimal('5'), Decimal('2'), add, Decimal('7'))

def test_subtract_operation():
    """
    Test the subtraction operation.
    """
    perform_and_check(Decimal('9'), Decimal('2'), subtract, Decimal('7'))

def test_multiply_operation():
    """
    Test the multiplication operation.
    """
    perform_and_check(Decimal('2'), Decimal('4'), multiply, Decimal('8'))

def test_divide_by_zero():
    """
    Test that division by zero raises a ValueError.
    """
    calc = Calculation.create(Decimal('7'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
