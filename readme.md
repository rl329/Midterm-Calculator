# Midterm Calculator

    ### Design Patterns

    The design patterns I used were the command pattern and Singleton Pattern throughout my code.

    ### Plugin System (Command Pattern)

    For starters, the command pattern is where I loadded my pluggins ('add', 'subtract', 'multiply', 'divivde').
    The purpose of the command patter is to perform an opertation as an object. In this case each plugin class would represent a tailored command.

- [Add Command](calculator_app/plugins/add_command.py): Performs the addition operation.
- [Subtract Command](calculator_app/plugins/subtract_command.py): Handles subtraction.
- [Multiply Command](calculator_app/plugins/multiply_command.py): Handles multiplication.
- [Divide Command](calculator_app/plugins/divide_command.py): Manages division operations.

    ### Singleton Design Pattern

    This design would ensure only a single history is maintained throughout the calculator session. This would help it keep clean and orgainzed and have everything be stored under one history.
    The calc_history.py code includes _history where it states that only one instance of the history exists across the program.

- [calc_history.py](calculator_app/calc_history.py)


    ### Environment variables

    I used the environment variables in my main.py with the dotenv library. The purpose of this is to manage configurations. In my project I am using configurtations such as API keys.
    The way it works is by loading the .env file.

- [main.py](main.py).














