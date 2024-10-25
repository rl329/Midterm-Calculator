from calculator_app.calculator import Calculator

def test_addition():
    """Test Calculator add function."""
    assert Calculator.add(4, 3) == 7

def test_subtraction():
    """Test Calculator subtract function."""
    assert Calculator.subtract(4, 3) == 1

def test_multiply():
    """Test Calculator multiply function."""
    assert Calculator.multiply(2, 2) == 4

def test_divide():
    """Test Calculator divide function."""
    assert Calculator.divide(2, 2) == 1
