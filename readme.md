# Midterm Calculator

* The design patterns I used were the command pattern and Singleton Pattern throughout my code.

    For starters, the command pattern is where I loadded my pluggins ('add', 'subtract', 'multiply', 'divivde').
    The purpose of the command patter is to perform an opertation as an object. In this case each plugin class would represent a tailored command.

    ### Plugin System (Command Pattern)

- [Add Command](calculator_app/plugins/add_command.py): Performs the addition operation.
- [Subtract Command](calculator_app/plugins/subtract_command.py): Handles subtraction.
- [Multiply Command](calculator_app/plugins/multiply_command.py): Handles multiplication.
- [Divide Command](calculator_app/plugins/divide_command.py): Manages division operations.

# Testing

1. pytest
2. pytest --pylint
3. pytest --pylint --cov









