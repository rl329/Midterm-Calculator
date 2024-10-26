# calculator_app/calc_operation.py

from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Add two numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Subtract two numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Multiply two numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Divide two numbers, raising an exception if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
