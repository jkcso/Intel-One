# This class is the main thread of the program, includes the welcome message function and the main function.
# Internal imports
import intro
import help
import search.engines as engines
import search.socialMedia as social
import search.edgar as edgar
import search.domains as domains
import search.shodan as shodan


# The main thread of the program.
if __name__ == '__main__':
    intro.welcomeMessage()

    # the main loop of the program running constantly until ctl+C or exit/quit is used.
    while True:
        # holds the current command of the user.
        userQuery = str(input('who-dis> '))

        # goes to help.
        if userQuery == 'help' or userQuery == '-h' or userQuery == '--help':
            help.help()

        # performs google search.
        elif userQuery.__contains__('-g') or userQuery.__contains__('--google'):
            engines.SearchEngines.googleSearch(userQuery)

        # performs search about posts on the given keyword in social search website looking in all available social media.
        elif userQuery.__contains__('-ss') or userQuery.__contains__('--social'):
            social.SocialMedia.retrievePosts(userQuery)

        # performs facebook search.
        elif userQuery.__contains__('-fb') or userQuery.__contains__('--facebook'):
            social.SocialMedia.retrieveAccounts(userQuery, 'fb')

        # performs linkedin search.
        elif userQuery.__contains__('-ln') or userQuery.__contains__('--linkedin'):
            social.SocialMedia.retrieveAccounts(userQuery, 'ln')

        # performs twitter search.
        elif userQuery.__contains__('-tw') or userQuery.__contains__('--twitter'):
            social.SocialMedia.retrieveAccounts(userQuery, 'tw')

        # performs instagram search.
        elif userQuery.__contains__('-in') or userQuery.__contains__('--instagram'):
            social.SocialMedia.retrieveAccounts(userQuery, 'in')

        # performs reddit search.
        elif userQuery.__contains__('-re') or userQuery.__contains__('--reddit'):
            social.SocialMedia.retrieveAccounts(userQuery, 're')

        # # Uses reddit username to get insights on lifetime reddit activity.
        elif userQuery.__contains__('-ure') or userQuery.__contains__('--userReddit'):
            social.SocialMedia.retrieveRedditUserStats(userQuery)

        # performs a search in www.pipl.com containing location information as well to be more specific.
        elif userQuery.__contains__('-p') and userQuery.__contains__('-l'):
            engines.PeopleSearchEngines.piplSearchLocation(userQuery)

        # performs a search in www.pipl.com to capture the social media not captured above.
        elif userQuery.__contains__('-p') or userQuery.__contains__('--pipl'):
            engines.PeopleSearchEngines.piplSearch(userQuery)

        # provides a link to search for companies in www.sec.gov.
        elif userQuery.__contains__('-e') or userQuery.__contains__('--edgar'):
            edgar.edgarSearch(userQuery)

        # provides a link to search for target domains in who.is website.
        elif userQuery.__contains__('-w') or userQuery.__contains__('--whois'):
            domains.Domains.whoIsSearch(userQuery)

        # provides a link to search in shodan.io.
        elif userQuery.__contains__('-sh') or userQuery.__contains__('--shodan'):
            shodan.shodanSearch(userQuery)

        # provides a link to search in asafaweb website for vulnerability scanning.
        elif userQuery.__contains__('-sc') or userQuery.__contains__('--scan'):
            domains.Domains.scanSearch(userQuery)

        # exits the program.
        elif userQuery == 'exit' or userQuery == 'quit':
            break

        # captures the case in which no option is matched and returns message to the user.
        else:
            errorString = " command not found, press 'help' to view the help menu."
            errorMessage = "'" + userQuery + "'" + errorString
            print(errorMessage)
