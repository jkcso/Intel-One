"""
Includes the help page of the program having information about the different flags and options.
Most importantly includes examples of how the different flags are going to be used.  This page
is going to be implemented iteratively i.e when a new feature is implemented this page is updated
to include info about it.
"""


# prints help into screen.
def help():
    menu = "\n" \
           "Please refer to 'Known technical issues' section in README.md file for any problems you have.\n" \
           "\n" \
           "-- [ Options for Help & Symbols Meaning ] --\n" \
           "\n" \
           "Options Short/Long  |  Description                                      |  Example                                 \n" \
           "=================== + ================================================= + =========================================\n" \
           "-h, --help          | Prints help on screen                             | who-dis> help | -h | --help              \n" \
           "'|' symbol          | Means 'or'                                        | who-dis> click 1 | 2 means click 1 or 2  \n" \
           "'-' symbol          | Used for the short flag                           | who-dis> john smith -g                   \n" \
           "'--' symbol         | Used for the long flag                            | who-dis> john smith --google             \n" \
           "\n" \
           "\n" \
           "-- [ Options for Individuals @ Social Media ] --\n" \
           "\n" \
           "Options Short/Long  |  Description                                      |  Example                                 \n" \
           "=================== + ================================================= + =========================================\n" \
           "-fb, --facebook     | Performs facebook search through google           | who-dis> john smith -fb | --facebook     \n" \
           "-ln, --linkedin     | Performs linkedin search through google           | who-dis> john smith -ln | --linkedin     \n" \
           "-tw, --twitter      | Performs twitter search through google            | who-dis> john smith -tw | --twitter      \n" \
           "-in, --instagram    | Performs instagram search through google          | who-dis> john smith -in | --instagram    \n" \
           "\n" \
           "\n" \
           "-- [ Options for Individuals @ (People) Search Engines ] --\n" \
           "\n" \
           "Options Short/Long  |  Description                                      |  Example                                 \n" \
           "=================== + ================================================= + =========================================\n" \
           "-g, --google        | Performs normal google search                     | who-dis> john smith -g | --google        \n" \
           "-p, --pipl          | Provided a link to pipl search engine             | who-dis> john smith -p | --pipl          \n" \
           "-p and -l           | Performs specific pipl using with location        | who-dis> john smith -p madrid -l         \n" \
           "\n" \
           "\n" \
           "-- [ Options for Companies @ Search Engines] --\n" \
           "\n" \
           "Options Short/Long  |  Description                                      |  Example                                 \n" \
           "=================== + ================================================= + =========================================\n" \
           "-g, --google        | Performs normal google search                     | who-dis> glovdi -g | --google            \n" \
           "-e, --edgar         | Performs search using edgar company search engine | who-dis> glovdi -e | --edgar             \n" \
           "\n" \
           "\n" \
           "-- [ Options for Companies @ Social Media] --\n" \
           "\n" \
           "Options Short/Long  |  Description                                      |  Example                                 \n" \
           "=================== + ================================================= + =========================================\n" \
           "-fb, --facebook     | Performs facebook search through google           | who-dis> glovdi -fb | --facebook         \n" \
           "-ln, --linkedin     | Performs linkedin search through google           | who-dis> glovdi -ln | --linkedin         \n" \
           "-tw, --twitter      | Performs twitter search through google            | who-dis> glovdi -tw | --twitter          \n" \
           "-in, --instagram    | Performs instagram search through google          | who-dis> glovdi -in | --instagram        \n" \
           "\n"
    print(menu)
