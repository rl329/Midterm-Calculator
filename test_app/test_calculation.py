from decimal import Decimal
import pytest
from calculator_app.calculation import Calculation
from calculator_app.calc_operation import add, subtract, multiply, divide

def test_addition_operation():
    """Test addition operation."""
    calc = Calculation.create(Decimal('3'), Decimal('2'), add)
    assert calc.perform() == Decimal('5')

def test_subtraction_operation():
    """Test subtraction operation."""
    calc = Calculation.create(Decimal('7'), Decimal('2'), subtract)
    assert calc.perform() == Decimal('5')

def test_multiplication_operation():
    """Test multiplication operation."""
    calc = Calculation.create(Decimal('4'), Decimal('2'), multiply)
    assert calc.perform() == Decimal('8')

def test_division_operation():
    """Test division operation."""
    calc = Calculation.create(Decimal('6'), Decimal('2'), divide)
    assert calc.perform() == Decimal('3')

def test_divide_by_zero():
    """Test division by zero raises a ValueError."""
    calc = Calculation.create(Decimal('7'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
