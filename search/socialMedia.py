import search.engines as engines
import search.utilities as util


# Class responsible for social media account collection of target user, company or domain.
class SocialMedia(object):
    # Advanced google dork used for returning results including the provided url.
    __INURL__ = " inurl:\""

    # Social media websites that are currently supported by Who-Dis.
    __FACEBOOK__ = "www.facebook.com\""
    __LINKEDIN__ = "www.linkedin.com\""
    __TWITTER__ = "www.twitter.com\""
    __INSTAGRAM__ = "www.instagram.com\""
    __REDDIT__ = "www.reddit.com\""

    # Performs social search through google using the advanced google dork inurl.
    def retrieveAccounts(query, media):
        # Parses the query to avoid the flag inclusion while performing google search.
        parsedQuery = util.Utilities.parseQuery(query)
        searchQuery = parsedQuery + SocialMedia.__INURL__

        # Searches in corresponding social media indicated by user.
        if media == 'fb':
            searchQuery += SocialMedia.__FACEBOOK__

        elif media == 'ln':
            searchQuery += SocialMedia.__LINKEDIN__

        elif media == 'tw':
            searchQuery += SocialMedia.__TWITTER__

        elif media == 'in':
            searchQuery += SocialMedia.__INSTAGRAM__

        elif media == 're':
            searchQuery += SocialMedia.__REDDIT__

        return engines.SearchEngines.googleSearch(searchQuery)

    # Used to retrieve posts about target from all available social media websites.
    def retrievePosts(query):
        parsedQuery = util.Utilities.parseQuery(query)
        postsLink_1 = 'https://www.social-searcher.com/social-buzz/?q5=' + parsedQuery
        postsLink_2 = 'https://www.social-searcher.com/google-social-search/?q=' + parsedQuery + '&fb=on&tw=on&gp=on&in=on&li=on&pi=on'
        print(postsLink_1)
        print(postsLink_2)
        print()

    # Uses reddit username to get insights on lifetime reddit activity.
    def retrieveRedditUserStats(query):
        redditLink = 'https://snoopsnoo.com/u/' + util.Utilities.parseQuery(query)
        print(redditLink)
        print()
