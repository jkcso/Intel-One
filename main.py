"""
This class is the main thread of the program, includes the welcome message function and the main function.
"""
# External imports

# Internal imports
import help


# Welcome screen of the program.
def welcomeMessage():
    message = "####################################################################\n" \
              "##                               _______                          ##\n" \
              "##         ||        ||  ||      ||   ||                          ##\n" \
              "##         ||    \   ||  ||      ||   ||  ___________             ##\n" \
              "##         ||   \ \  ||  ||____  ||   ||  |__________|_           ##\n" \
              "##         ||\ \  \ \||  ||   || ||___||   |___________|          ##\n" \
              "##         ||________||  ||   || ||___||                          ##\n" \
              "##                                                                ##\n" \
              "##           __      _   -------\          _________              ##\n" \
              "##         ||  \    |_|  \ \-----\        / /    / /              ##\n" \
              "##         ||   \         \ \             \_\   / /               ##\n" \
              "##         ||   /   ||     \ \                 / /                ##\n" \
              "##         ||  /    ||     / /                /_/                 ##\n" \
              "##         || /_____||____/ /                                     ##\n" \
              "##         ||/______||_____/                  |_|                 ##\n" \
              "##                                                                ##\n" \
              "####################################################################\n" \
              "Version 1.0\n" \
              "\n" \
              "Please press 'help' for user manual and options.\n" \
              "Press exit or quit to exit the program\n" \
              "Joseph Katsioloudes, 2017.\n" \
              "\n"
    print(message)


if __name__ == '__main__':
    welcomeMessage()

    # the main loop of the program running constantly until ctl+C or exit/quit is used.
    while True:
        # holds the current command of the user.
        userCommand = str(input('who-dis> '))

        # goes to help.
        if userCommand == 'help' or userCommand == '-h' or userCommand == '--help':
            help.help()
        # exits the program.
        elif userCommand == 'exit' or userCommand == 'quit':
            break