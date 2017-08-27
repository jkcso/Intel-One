"""
Includes the help page of the program having information about the different flags and options.
Most importantly includes examples of how the different flags are going to be used.  This page
is going to be implemented iteratively i.e when a new feature is implemented this page is updated
to include info about it.
"""


# prints help into screen.
def help():
    menu = "\n" \
           "- [options] -\n" \
           "\n" \
           "Options Short/Long  |  Description                                  |  Example                                 \n" \
           "=================== + ============================================= + =========================================\n" \
           "-h, --help          | Prints help on screen                         | who-dis> help                            \n" \
           "-g, --google        | Performs normal google search                 | who-dis> apple -g, steve jobs --google   \n" \
           "-fb, --facebook     | Performs facebook search through google       | who-dis> jon snow -fb                    \n" \
           "-ln, --linkedin     | Performs linkedin search through google       | who-dis> kevin spacey -ln                \n" \
           "-tw, --twitter      | Performs twitter search through google        | who-dis> beyonce -tw, beyonce --twitter  \n" \
           "-in, --instagram    | Performs instagram search through google      | who-dis> jetbrains -in                   \n" \
           "-p, --pipl          | Provided a link to www.pipl.com               | who-dis> jon snow -p, jon snow --pipl    \n" \
           "A -p B -l           | Performs www.pipl.com search with location    | who-dis> peter smith -p madrid -l        \n" \
           "-e, --edgar         | Performs search in www.sec.gov for companies  | who-dis> golman sachs -e                 \n" \
           "\n"
    print(menu)
