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
        emailQuery = engines.EmailValidityEngine(userQuery)
        otherQuery = other.Other(userQuery)

        # provides help to the user.
        if userQuery == 'help':
            help.help()

        # SOCIAL MEDIA
        # performs real time search on posts about given keyword.
        elif parsedUserQuery[effectiveLen] == '-rts' or parsedUserQuery[effectiveLen] == '--rtsearch':
            social.SocialMedia.realTimeSocialMediaSearch(socialQuery)

        # performs facebook search.
        elif parsedUserQuery[effectiveLen] == '-fb' or parsedUserQuery[effectiveLen] == '--facebook':
            social.SocialMedia.retrieveAccounts(socialQuery, 'fb')

        # performs linkedin search.
        elif parsedUserQuery[effectiveLen] == '-ln' or parsedUserQuery[effectiveLen] == '--linkedin':
            social.SocialMedia.retrieveAccounts(socialQuery, 'ln')
            print("Browser plugin that finds emails of people's profiles in Linkedin.")
            print('https://chrome.google.com/webstore/detail/ftl/lkpekgkhmldknbcgjicjkomphkhhdkjj?hl=en-GB\n')

        # performs twitter search.
        elif parsedUserQuery[effectiveLen] == '-tw' or parsedUserQuery[effectiveLen] == '--twitter':
            social.SocialMedia.retrieveAccounts(socialQuery, 'tw')
            social.SocialMedia.retrieveTweets(socialQuery)
            social.SocialMedia.retrieveTwitterAnalytics(socialQuery)

        # performs instagram search.
        elif parsedUserQuery[effectiveLen] == '-in' or parsedUserQuery[effectiveLen] == '--instagram':
            social.SocialMedia.retrieveAccounts(socialQuery, 'in')
            social.SocialMedia.retrieveInstagramPosts(socialQuery)

        # performs pinterest search.
        elif parsedUserQuery[effectiveLen] == '-pn' or parsedUserQuery[effectiveLen] == '--pinterest':
            social.SocialMedia.retrieveAccounts(socialQuery, 'pn')

        # performs tumblr search.
        elif parsedUserQuery[effectiveLen] == '-tb' or parsedUserQuery[effectiveLen] == '--tumblr':
            social.SocialMedia.retrieveAccounts(socialQuery, 'tb')

        # performs reddit search.
        elif parsedUserQuery[effectiveLen] == '-re' or parsedUserQuery[effectiveLen] == '--reddit':
            social.SocialMedia.retrieveAccounts(socialQuery, 're')
            social.SocialMedia.retrieveRedditPosts(socialQuery)

        # Uses reddit username to get insights on lifetime reddit activity.
        elif parsedUserQuery[effectiveLen] == '-ure' or parsedUserQuery[effectiveLen] == '--userReddit':
            social.SocialMedia.retrieveRedditUserStats(socialQuery)

        # Searches for user's published work in source code search and github.
        elif parsedUserQuery[effectiveLen] == '-cd' or parsedUserQuery[effectiveLen] == '--code':
            social.SocialMedia.sourceCodeSearch(socialQuery)

        # Searches for individuals or company profiles in youtube.
        elif parsedUserQuery[effectiveLen] == '-yt' or parsedUserQuery[effectiveLen] == '--youtube':
            social.SocialMedia.youtubeSearch(socialQuery)

        # Searches for additional videos on other multiple video database about individuals or company profiles.
        elif parsedUserQuery[effectiveLen] == '-evs' or parsedUserQuery[effectiveLen] == '--extraVid':
            social.SocialMedia.otherVdieoSearch(socialQuery)

        # Searches for target keyword in blogs.
        elif parsedUserQuery[effectiveLen] == '-bl' or parsedUserQuery[effectiveLen] == '--blogs':
            social.SocialMedia.blogSearch(socialQuery)

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

        # performs keyword matching search engine.
        elif parsedUserQuery[effectiveLen] == '-km' or parsedUserQuery[effectiveLen] == '--keyword':
            engines.SearchEngines.keywordMatching(searchEngineQuery)

        # performs clustering search.
        elif parsedUserQuery[effectiveLen] == '-cl' or parsedUserQuery[effectiveLen] == '--cluster':
            engines.SearchEngines.clusteringSearchEngines(searchEngineQuery)

        # performs excite news search.
        elif parsedUserQuery[effectiveLen] == '-ex' or parsedUserQuery[effectiveLen] == '--exciteNews':
            engines.SearchEngines.exciteNewsSearch(searchEngineQuery)

        # performs old posts serach in factbites search engine.
        elif parsedUserQuery[effectiveLen] == '-oa' or parsedUserQuery[effectiveLen] == '--oldArticles':
            engines.SearchEngines.oldArticlesSearch(searchEngineQuery)

        # performs old posts serach in factbites search engine.
        elif parsedUserQuery[effectiveLen] == '-rss' or parsedUserQuery[effectiveLen] == '--rssFeeds':
            engines.SearchEngines.searchRSS(searchEngineQuery)

        # PEOPLE SEARCH ENGINES
        # performs a search in www.pipl.com to capture the social media not captured above.
        elif parsedUserQuery[effectiveLen] == '-p' or parsedUserQuery[effectiveLen] == '--people':
            engines.PeopleSearchEngines.peopleSearch(peopleSearchQuery)

        # performs a search in www.pipl.com containing location information as well to be more specific.
        elif userQuery.__contains__('-p') and userQuery.__contains__('-l'):
            engines.PeopleSearchEngines.piplSearchLocation(peopleSearchQuery, '-p')

        # EMAIL VALIDITY ENGINE
        # performs email validity search using provided address.
        elif parsedUserQuery[effectiveLen] == '-ev' or parsedUserQuery[effectiveLen] == '--emailValid':
            engines.EmailValidityEngine.emailValidity(emailQuery)

        # COMPANIES
        # Provides link to corporate wiki that includes a lot of information about a target company.
        elif parsedUserQuery[effectiveLen] == '-cs' or parsedUserQuery[effectiveLen] == '--compSearch':
            companies.Companies.companySearch(companiesQuery)

        # Provides link to annual reports, slideshows and other insights of a company.
        elif parsedUserQuery[effectiveLen] == '-are' or parsedUserQuery[effectiveLen] == '--reports':
            companies.Companies.annualReportSearch(companiesQuery)

        # Gets the company email format.
        elif parsedUserQuery[effectiveLen] == '-cef' or parsedUserQuery[effectiveLen] == '--emailFormat':
            companies.Companies.getCompanyEmailFormat(companiesQuery)

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

        # provides a link to search with what technologies is the website build with.
        elif parsedUserQuery[effectiveLen] == '-bw' or parsedUserQuery[effectiveLen] == '--builtWith':
            domains.Domains.builtWith(domainQuery)

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

        # Performs all possible searches about a given email format.
        elif parsedUserQuery[effectiveLen] == '-e' or parsedUserQuery[effectiveLen] == '--email':
            engines.EmailValidityEngine.emailSearch(emailQuery)
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
