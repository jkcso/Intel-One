# This class is the main thread of the program, includes the welcome message function and the main function.
# Internal imports
import intro
import help
import search.engines as engines
import search.socialMedia as social
import search.companies as companies
import search.domains as domains
import search.other as other

__listLastIndex__ = 1

# The main thread of the program.
if __name__ == '__main__':
    intro.welcomeMessage()

    # the main loop of the program running constantly until ctl+C or exit/quit is used.
    while True:
        # holds the current command of the user.
        userQuery = str(input('who-dis> '))
        parsedUserQuery = userQuery.split(' ')
        lenUserQuery = len(parsedUserQuery)
        effectiveLen = lenUserQuery - __listLastIndex__

        # provides help to the user.
        if userQuery == 'help':
            help.help()

        # SOCIAL MEDIA
        # performs search about posts on the given keyword in social search website looking in all available social media.
        elif parsedUserQuery[effectiveLen] == '-ss' or parsedUserQuery[effectiveLen] == '--social':
            social.SocialMedia.retrievePosts(userQuery)

        # performs facebook search.
        elif parsedUserQuery[effectiveLen] == '-fb' or parsedUserQuery[effectiveLen] == '--facebook':
            social.SocialMedia.retrieveAccounts(userQuery, 'fb')

        # performs linkedin search.
        elif parsedUserQuery[effectiveLen] == '-ln' or parsedUserQuery[effectiveLen] == '--linkedin':
            social.SocialMedia.retrieveAccounts(userQuery, 'ln')

        # performs twitter search.
        elif parsedUserQuery[effectiveLen] == '-tw' or parsedUserQuery[effectiveLen] == '--twitter':
            social.SocialMedia.retrieveAccounts(userQuery, 'tw')

        # performs instagram search.
        elif parsedUserQuery[effectiveLen] == '-in' or parsedUserQuery[effectiveLen] == '--instagram':
            social.SocialMedia.retrieveAccounts(userQuery, 'in')

        # performs reddit search.
        elif parsedUserQuery[effectiveLen] == '-re' or parsedUserQuery[effectiveLen] == '--reddit':
            social.SocialMedia.retrieveAccounts(userQuery, 're')

        # Uses reddit username to get insights on lifetime reddit activity.
        elif parsedUserQuery[effectiveLen] == '-ure' or parsedUserQuery[effectiveLen] == '--userReddit':
            social.SocialMedia.retrieveRedditUserStats(userQuery)

        # Searches for user's published work in Github.
        elif parsedUserQuery[effectiveLen] == '-gh' or parsedUserQuery[effectiveLen] == '--github':
            social.SocialMedia.githubSearch(userQuery)

        # SEARCH ENGINES
        # performs google search.
        elif parsedUserQuery[effectiveLen] == '-g' or parsedUserQuery[effectiveLen] == '--google':
            engines.SearchEngines.googleSearch(userQuery)

        # performs duckduckgo search.
        elif parsedUserQuery[effectiveLen] == '-ddg' or parsedUserQuery[effectiveLen] == '--ddGo':
            engines.SearchEngines.ddGoSearch(userQuery)

        # performs baidu search.
        elif parsedUserQuery[effectiveLen] == '-bd' or parsedUserQuery[effectiveLen] == '--baidu':
            engines.SearchEngines.baiduSearch(userQuery)

        # performs bing search.
        elif parsedUserQuery[effectiveLen] == '-bg' or parsedUserQuery[effectiveLen] == '--bing':
            engines.SearchEngines.bingSearch(userQuery)

        # PEOPLE SEARCH ENGINES
        # performs a search in www.pipl.com to capture the social media not captured above.
        elif parsedUserQuery[effectiveLen] == '-p' or parsedUserQuery[effectiveLen] == '--pipl':
            engines.PeopleSearchEngines.piplSearch(userQuery)

        # performs a search in www.pipl.com containing location information as well to be more specific.
        elif userQuery.__contains__('-p') and userQuery.__contains__('-l'):
            engines.PeopleSearchEngines.piplSearchLocation(userQuery)

        # COMPANIES
        # provides a link to search for companies in www.sec.gov.
        elif parsedUserQuery[effectiveLen] == '-ed' or parsedUserQuery[effectiveLen] == '--edgar':
            companies.Companies.edgarSearch(userQuery)

        # Provides link to corporate wiki that includes a lot of information about a target company.
        elif parsedUserQuery[effectiveLen] == '-cw' or parsedUserQuery[effectiveLen] == '--corpWiki':
            companies.Companies.corpWikiSearch(userQuery)

        # Provides link to annual reports, slideshows and other insights of a company.
        elif parsedUserQuery[effectiveLen] == '-ar' or parsedUserQuery[effectiveLen] == '--reports':
            companies.Companies.annualReportSearch(userQuery)

        # DOMAINS
        # provides a link to search for target domains in who.is website.
        elif parsedUserQuery[effectiveLen] == '-wh' or parsedUserQuery[effectiveLen] == '--whois':
            domains.Domains.whoIsSearch(userQuery)

        # provides a link to search in asafaweb website for vulnerability scanning.
        elif parsedUserQuery[effectiveLen] == '-sc' or parsedUserQuery[effectiveLen] == '--scan':
            domains.Domains.scanSearch(userQuery)

        # provides a link to search in archive.org website for past versions of target domain.
        elif parsedUserQuery[effectiveLen] == '-ar' or parsedUserQuery[effectiveLen] == '--archive':
            domains.Domains.archiveSearch(userQuery)

        # provides a link to view the robots file of a website.
        elif parsedUserQuery[effectiveLen] == '-rb' or parsedUserQuery[effectiveLen] == '--robots':
            domains.Domains.robotsView(userQuery)

        # OTHER
        # provides a link to search in shodan.io.
        elif parsedUserQuery[effectiveLen] == '-sh' or parsedUserQuery[effectiveLen] == '--shodan':
            other.Other.shodanSearch(userQuery)

        # exits the program.
        elif userQuery == 'exit' or userQuery == 'quit':
            break

        # captures the case in which no option is matched and returns message to the user.
        else:
            errorString = " command not found, press 'help' to view the help menu."
            errorMessage = "'" + userQuery + "'" + errorString
            print(errorMessage)
            print()
