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

        # objects needed later for iterative commands that perform all searches in one command.
        # also provide isolation for specific class category inside 'search' directory.
        socialQuery = social.SocialMedia(userQuery)
        searchEngineQuery = engines.SearchEngines(userQuery)
        peopleSearchQuery = engines.PeopleSearchEngines(userQuery)
        companiesQuery = companies.Companies(userQuery)
        domainQuery = domains.Domains(userQuery)
        otherQuery = other.Other(userQuery)

        # provides help to the user.
        if userQuery == 'help':
            help.help()

        # SOCIAL MEDIA
        # performs search about posts on the given keyword in social search website looking in all available social media.
        elif parsedUserQuery[effectiveLen] == '-ss' or parsedUserQuery[effectiveLen] == '--social':
            social.SocialMedia.retrievePosts(socialQuery)

        # performs facebook search.
        elif parsedUserQuery[effectiveLen] == '-fb' or parsedUserQuery[effectiveLen] == '--facebook':
            social.SocialMedia.retrieveAccounts(socialQuery, 'fb')

        # performs linkedin search.
        elif parsedUserQuery[effectiveLen] == '-ln' or parsedUserQuery[effectiveLen] == '--linkedin':
            social.SocialMedia.retrieveAccounts(socialQuery, 'ln')

        # performs twitter search.
        elif parsedUserQuery[effectiveLen] == '-tw' or parsedUserQuery[effectiveLen] == '--twitter':
            social.SocialMedia.retrieveAccounts(socialQuery, 'tw')

        # performs instagram search.
        elif parsedUserQuery[effectiveLen] == '-in' or parsedUserQuery[effectiveLen] == '--instagram':
            social.SocialMedia.retrieveAccounts(socialQuery, 'in')

        # performs reddit search.
        elif parsedUserQuery[effectiveLen] == '-re' or parsedUserQuery[effectiveLen] == '--reddit':
            social.SocialMedia.retrieveAccounts(socialQuery, 're')

        # Uses reddit username to get insights on lifetime reddit activity.
        elif parsedUserQuery[effectiveLen] == '-ure' or parsedUserQuery[effectiveLen] == '--userReddit':
            social.SocialMedia.retrieveRedditUserStats(socialQuery)

        # Searches for user's published work in Github.
        elif parsedUserQuery[effectiveLen] == '-gh' or parsedUserQuery[effectiveLen] == '--github':
            social.SocialMedia.githubSearch(socialQuery)

        # Searches for individuals or company profiles in youtube.
        elif parsedUserQuery[effectiveLen] == '-yt' or parsedUserQuery[effectiveLen] == '--youtube':
            social.SocialMedia.youtubeSearch(socialQuery)

        # SEARCH ENGINES
        # performs google search.
        elif parsedUserQuery[effectiveLen] == '-g' or parsedUserQuery[effectiveLen] == '--google':
            engines.SearchEngines.googleSearch(searchEngineQuery)

        # performs duckduckgo search.
        elif parsedUserQuery[effectiveLen] == '-ddg' or parsedUserQuery[effectiveLen] == '--ddGo':
            engines.SearchEngines.ddGoSearch(searchEngineQuery)

        # performs baidu search.
        elif parsedUserQuery[effectiveLen] == '-bd' or parsedUserQuery[effectiveLen] == '--baidu':
            engines.SearchEngines.baiduSearch(searchEngineQuery)

        # performs bing search.
        elif parsedUserQuery[effectiveLen] == '-bg' or parsedUserQuery[effectiveLen] == '--bing':
            engines.SearchEngines.bingSearch(searchEngineQuery)

        # performs qwant search.
        elif parsedUserQuery[effectiveLen] == '-qw' or parsedUserQuery[effectiveLen] == '--qwant':
            engines.SearchEngines.qwantSearch(searchEngineQuery)

        # performs excite news search.
        elif parsedUserQuery[effectiveLen] == '-ex' or parsedUserQuery[effectiveLen] == '--exciteNews':
            engines.SearchEngines.exciteNewsSearch(searchEngineQuery)

        # performs old posts serach in factbites search engine.
        elif parsedUserQuery[effectiveLen] == '-oa' or parsedUserQuery[effectiveLen] == '--oldArticles':
            engines.SearchEngines.oldArticlesSearch(searchEngineQuery)

        # PEOPLE SEARCH ENGINES
        # performs a search in www.pipl.com to capture the social media not captured above.
        elif parsedUserQuery[effectiveLen] == '-p' or parsedUserQuery[effectiveLen] == '--pipl':
            engines.PeopleSearchEngines.piplSearch(peopleSearchQuery)

        # performs a search in www.pipl.com containing location information as well to be more specific.
        elif userQuery.__contains__('-p') and userQuery.__contains__('-l'):
            engines.PeopleSearchEngines.piplSearchLocation(peopleSearchQuery, '-p')

        # COMPANIES
        # provides a link to search for companies in www.sec.gov.
        elif parsedUserQuery[effectiveLen] == '-ed' or parsedUserQuery[effectiveLen] == '--edgar':
            companies.Companies.edgarSearch(companiesQuery)

        # Provides link to corporate wiki that includes a lot of information about a target company.
        elif parsedUserQuery[effectiveLen] == '-cw' or parsedUserQuery[effectiveLen] == '--corpWiki':
            companies.Companies.corpWikiSearch(companiesQuery)

        # Provides link to annual reports, slideshows and other insights of a company.
        elif parsedUserQuery[effectiveLen] == '-are' or parsedUserQuery[effectiveLen] == '--reports':
            companies.Companies.annualReportSearch(companiesQuery)

        # DOMAINS
        # provides a link to search for target domains in who.is website.
        elif parsedUserQuery[effectiveLen] == '-wh' or parsedUserQuery[effectiveLen] == '--whois':
            domains.Domains.whoIsSearch(domainQuery)

        # provides a link that performs a DNS lookup.
        elif parsedUserQuery[effectiveLen] == '-dns' or parsedUserQuery[effectiveLen] == '--dnsLookup':
            domains.Domains.dnsLookup(domainQuery)

        # provides a link to search in asafaweb website for vulnerability scanning.
        elif parsedUserQuery[effectiveLen] == '-sc' or parsedUserQuery[effectiveLen] == '--scan':
            domains.Domains.scanSearch(domainQuery)

        # provides a link to search in archive.org website for past versions of target domain.
        elif parsedUserQuery[effectiveLen] == '-ar' or parsedUserQuery[effectiveLen] == '--archive':
            domains.Domains.archiveSearch(domainQuery)

        # provides a link to view the robots file of a website.
        elif parsedUserQuery[effectiveLen] == '-rb' or parsedUserQuery[effectiveLen] == '--robots':
            domains.Domains.robotsView(domainQuery)

        # OTHER
        # provides a link to search in shodan.io.
        elif parsedUserQuery[effectiveLen] == '-sh' or parsedUserQuery[effectiveLen] == '--shodan':
            other.Other.shodanSearch(otherQuery)

        # POWERFUL ALL IN ONE SEARCH divided into categories.
        # Performs all possible searches about a company.
        elif parsedUserQuery[effectiveLen] == '-c' or parsedUserQuery[effectiveLen] == '--company':
            companies.Companies.companyAllSearches(companiesQuery)
            social.SocialMedia.socialMediaAllSearches(socialQuery)
            engines.SearchEngines.searchEngineAllSearches(searchEngineQuery)

        # Performs all possible searches about a target domain.
        elif parsedUserQuery[effectiveLen] == '-d' or parsedUserQuery[effectiveLen] == '--domain':
            domains.Domains.domainAllSearches(domainQuery)
            social.SocialMedia.socialMediaAllSearches(socialQuery)
            engines.SearchEngines.searchEngineAllSearches(searchEngineQuery)

        # Performs all possible searches about an individual.
        elif parsedUserQuery[effectiveLen] == '-i' or parsedUserQuery[effectiveLen] == '--individual':
            engines.PeopleSearchEngines.peopleEngineAllSearches(peopleSearchQuery)
            social.SocialMedia.socialMediaAllSearches(socialQuery)
            engines.SearchEngines.searchEngineAllSearches(searchEngineQuery)

        # Performs all possible searches about an individual.
        elif userQuery.__contains__('-i') and userQuery.__contains__('-l'):
            engines.PeopleSearchEngines.peopleEngineAllSearches(peopleSearchQuery)
            social.SocialMedia.socialMediaAllSearches(socialQuery)
            engines.SearchEngines.searchEngineAllSearches(searchEngineQuery)

        # Performs all possible searches in social media.
        elif parsedUserQuery[effectiveLen] == '-sm' or parsedUserQuery[effectiveLen] == '--socialMedia':
            social.SocialMedia.socialMediaAllSearches(socialQuery)

        # Performs all possible searches about anything in all search engines.
        elif parsedUserQuery[effectiveLen] == '-s' or parsedUserQuery[effectiveLen] == '--search':
            engines.SearchEngines.searchEngineAllSearches(searchEngineQuery)

        # exits the program.
        elif userQuery == 'exit' or userQuery == 'quit':
            break

        # captures the case in which no option is matched and returns message to the user.
        else:
            errorString = " command not found, press 'help' to view the help menu."
            errorMessage = "'" + userQuery + "'" + errorString
            print(errorMessage)
            print()
