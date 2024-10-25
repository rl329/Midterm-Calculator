"""
This module contains tests for the Calculator class.
"""

from calculator_app.calculator import Calculator

def test_addition():
    """
    Test that the addition function returns the correct result.
    """
    assert Calculator.add(4, 3) == 7

def test_subtraction():
    """
    Test that the subtraction function returns the correct result.
    """
    assert Calculator.subtract(4, 3) == 1

def test_multiplication():
    """
    Test that the multiplication function returns the correct result.
    """
    assert Calculator.multiply(2, 2) == 4

def test_division():
    """
    Test that the division function returns the correct result.
    """
    assert Calculator.divide(2, 2) == 1
