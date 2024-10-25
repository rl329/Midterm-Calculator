"""
This module contains tests for the CalcHistory class.
"""
# pylint: disable=redefined-outer-name

from decimal import Decimal
import pytest
from calculator_app.calc_history import CalcHistory
from calculator_app.calculation import Calculation
from calculator_app.calc_operation import add

@pytest.fixture
def setup_history():
    """
    Setup fixture to clear history and add sample calculations.
    """
    CalcHistory.clear_history()
    CalcHistory.add_calculation(Calculation.create(Decimal('3'), Decimal('2'), add))

def test_add_calculation(setup_history):  # pylint: disable=unused-argument
    """
    Test adding a calculation to the history.
    """
    calc = Calculation.create(Decimal('4'), Decimal('2'), add)
    CalcHistory.add_calculation(calc)
    assert CalcHistory.get_latest() == calc

def test_clear_history():
    """
    Test clearing the entire history.
    """
    CalcHistory.clear_history()
    assert len(CalcHistory.get_history()) == 0

def test_get_latest(setup_history):  # pylint: disable=unused-argument
    """
    Test retrieving the latest calculation from the history.
    """
    latest = CalcHistory.get_latest()
    assert latest.a == Decimal('3') and latest.b == Decimal('2')
