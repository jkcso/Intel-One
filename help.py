"""
Includes the help page of the program having information about the different flags and options.
Most importantly includes examples of how the different flags are going to be used.  This page
is going to be implemented iteratively i.e when a new feature is implemented this page is updated
to include info about it.
"""

# prints help into screen.
def help():
    menu = "- [options] -\n" \
           "\n" \
           "Options Short/Long  |  Description                     |  Example                        \n" \
           "=================== + ================================ + ================================\n" \
           "-h, --help          | Prints help on screen            | who-dis -h, who-dis --help      \n" \
           "\n"
    print(menu)
