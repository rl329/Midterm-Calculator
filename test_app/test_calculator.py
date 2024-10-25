from decimal import Decimal
from calculator_app.calculator import Calculator
from calculator_app.calc_history import CalcHistory

def test_add():
    """Test the add method."""
    assert Calculator.add(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract():
    """Test the subtract method."""
    assert Calculator.subtract(Decimal('5'), Decimal('2')) == Decimal('3')

def test_multiply():
    """Test the multiply method."""
    assert Calculator.multiply(Decimal('3'), Decimal('4')) == Decimal('12')

def test_divide():
    """Test the divide method."""
    assert Calculator.divide(Decimal('10'), Decimal('2')) == Decimal('5')

def test_divide_by_zero():
    """Test that division by zero raises an exception."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(Decimal('5'), Decimal('0'))

def test_calculation_history():
    """Test adding a calculation to history."""
    Calculator.add(Decimal('1'), Decimal('1'))
    assert len(CalcHistory.get_history()) == 1

def test_clear_history():
    """Test clearing the history."""
    Calculator.add(Decimal('2'), Decimal('2'))
    CalcHistory.clear_history()
    assert len(CalcHistory.get_history()) == 0
