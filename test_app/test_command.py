"""
This module contains tests for the command classes of the calculator.
"""

from decimal import Decimal  # Standard library imports

import pytest  # Third-party imports

from calculator_app.command import (  # Local application imports
    AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand
)
from calculator_app.calculator import Calculator

def test_add_command():
    """Test the AddCommand executes correctly."""
    calculator = Calculator()
    command = AddCommand(calculator, Decimal('2'), Decimal('3'))
    result = command.execute()
    assert result == Decimal('5')

def test_subtract_command():
    """Test the SubtractCommand executes correctly."""
    calculator = Calculator()
    command = SubtractCommand(calculator, Decimal('5'), Decimal('3'))
    result = command.execute()
    assert result == Decimal('2')

def test_multiply_command():
    """Test the MultiplyCommand executes correctly."""
    calculator = Calculator()
    command = MultiplyCommand(calculator, Decimal('4'), Decimal('2'))
    result = command.execute()
    assert result == Decimal('8')

def test_divide_command():
    """Test the DivideCommand executes correctly."""
    calculator = Calculator()
    command = DivideCommand(calculator, Decimal('10'), Decimal('2'))
    result = command.execute()
    assert result == Decimal('5')

def test_divide_by_zero():
    """Test that division by zero raises a ZeroDivisionError."""
    calculator = Calculator()
    command = DivideCommand(calculator, Decimal('5'), Decimal('0'))
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        command.execute()

def test_menu_command(capsys):
    """Test the MenuCommand displays available commands."""
    menu = MenuCommand(["add", "subtract", "multiply", "divide", "quit"])
    menu.execute()

    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "- add" in captured.out
    assert "- subtract" in captured.out
    assert "- multiply" in captured.out
    assert "- divide" in captured.out
    assert "- quit" in captured.out
