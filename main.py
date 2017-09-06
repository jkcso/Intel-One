# This class is the main thread of the program, includes the welcome message function and the main function.
# External imports

# Internal imports
import help
import search.google as google
import search.socialMedia as socialMedia
import search.pipl as pipl
import search.edgar as edgar
import search.whois as whois
import search.shodan as shodan
import search.scanner as scanner
import search.reddit as reddit


# Welcome screen of the program.
def _welcomeMessage():
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
              "Please refer to 'Known technical issues' section in README.md file for any problems you have.\n" \
              "\n" \
              "Written by Joseph Katsioloudes, 2017.\n" \
              "\n"
    print(message)


# The main thread of the program.
if __name__ == '__main__':
    _welcomeMessage()

    # the main loop of the program running constantly until ctl+C or exit/quit is used.
    while True:
        # holds the current command of the user.
        userCommand = str(input('who-dis> '))

        # goes to help.
        if userCommand == 'help' or userCommand == '-h' or userCommand == '--help':
            help.help()

        # performs google search.
        elif userCommand.__contains__('-g') or userCommand.__contains__('--google'):
            google.googleSearch(userCommand)

        # performs facebook search.
        elif userCommand.__contains__('-fb') or userCommand.__contains__('--facebook'):
            socialMedia.facebookSearch(userCommand)

        # performs linkedin search.
        elif userCommand.__contains__('-ln') or userCommand.__contains__('--linkedin'):
            socialMedia.linkedinSearch(userCommand)

        # performs twitter search.
        elif userCommand.__contains__('-tw') or userCommand.__contains__('--twitter'):
            socialMedia.twitterSearch(userCommand)

        # performs instagram search.
        elif userCommand.__contains__('-in') or userCommand.__contains__('--instagram'):
            socialMedia.instagramSearch(userCommand)

        # performs reddit search.
        elif userCommand.__contains__('-re') or userCommand.__contains__('--reddit'):
            socialMedia.redditSearch(userCommand)

        # performs search about posts on the given keyword in social search website looking in all available social media.
        elif userCommand.__contains__('-ss') or userCommand.__contains__('--social'):
            socialMedia.SocialSearcher.ssSearch(userCommand)

        # performs a search in www.pipl.com containing location information as well to be more specific.
        elif userCommand.__contains__('-p') and userCommand.__contains__('-l'):
            pipl.piplSearchLocation(userCommand)

        # performs a search in www.pipl.com to capture the social media not captured above.
        elif userCommand.__contains__('-p') or userCommand.__contains__('--pipl'):
            pipl.piplSearch(userCommand)

        # provides a link to search for companies in www.sec.gov.
        elif userCommand.__contains__('-e') or userCommand.__contains__('--edgar'):
            edgar.edgarSearch(userCommand)

        # provides a link to search for target domains in who.is website.
        elif userCommand.__contains__('-w') or userCommand.__contains__('--whois'):
            whois.whoIsSearch(userCommand)

        # provides a link to search in shodan.io.
        elif userCommand.__contains__('-sh') or userCommand.__contains__('--shodan'):
            shodan.shodanSearch(userCommand)

        # provides a link to search in asafaweb website for vulnerability scanning.
        elif userCommand.__contains__('-sc') or userCommand.__contains__('--scan'):
            scanner.scanSearch(userCommand)

        # # Uses reddit username to get insights on lifetime reddit activity.
        elif userCommand.__contains__('-reU') or userCommand.__contains__('--redditUser'):
            reddit.redditSearch(userCommand)

        # exits the program.
        elif userCommand == 'exit' or userCommand == 'quit':
            break

        # captures the case in which no option is matched and returns message to the user.
        else:
            errorString = " command not found, press 'help' to view the help menu."
            errorMessage = "'" + userCommand + "'" + errorString
            print(errorMessage)
