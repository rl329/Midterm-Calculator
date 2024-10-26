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

- [calc_history.py](calculator_app/calc_history.py): Calculator History code.

    ### Environment variables

    I used the environment variables in my main.py with the dotenv library. The purpose of this is to manage configurations. In my project I am using configurtations such as API keys.
    The way it works is by loading the .env file. The .env file is part of my .gitignore however I would provide a link to my .gitignore and .env file.

- [main.py](main.py): The main program.
- [.gitignore](.gitignore): The .gitignore used throughout my program.
- [.env](.env): The .env file I created were it would display the API Keys. etc.

    ### Logging

    I used logging in my main.py program as well. The way logging was implented was through the logging library, however I designed it where everytime the program begins to log it would store the information in a seprate file
    know as 'app.log'.
    The purpose of logging is to log information, errors, warnings in order to track events for debugging or auditing purposes.
    The app.log would capture runtime logs, such as saving and loading hsitory.

- [main.py](main.py): The main program.
- [app.log](app.log): The separate application log file.


    ### Usage of Try/Catch/Exceptions (LBYL and EAFP)

    In my program I implented both LBYL and EAFP. Both of these were implemented in my calc_history.py file.
    The 'Look Before You Leap' would check if a condition is true befoe taking action toa void rasing exceptions.
    Meanwhile, the 'Easier to Ask for Forgiveness than Permission' would try an operation directly and handles exceptions if they occur.

-[Calculator History](calculator_app/calc_history.py): Calculator History code.











