"""
This module contains test configurations and data generators for the calculator tests.
"""

from decimal import Decimal
from faker import Faker
from calculator_app.calc_operation import add, subtract, multiply, divide

# Initialize the Faker instance for generating test data
fake = Faker()

def generate_test_data(num_records: int):
    """
    Generate test data for calculator operations.
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        # Ensure 'b' is non-zero to avoid division-by-zero errors
        b = Decimal(fake.random_number(digits=2)) or Decimal('1')
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        expected = operation_func(a, b)

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """
    Add a command line option for the number of test records.
    """
    parser.addoption(
        "--num-records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    """
    Generate parameterized tests based on generated data.
    """
    if {"a", "b", "expected"}.intersection(metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("a, b, operation, expected", parameters)
