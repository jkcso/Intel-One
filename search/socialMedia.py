# imports the google wrapper class defined in this directory.
import search.google as google
# imports utilities class for performing parsing or spacing arrangements.
import search.utilities as util


# Responsible for social media account collection of target user, company or domain.
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

        return google.googleSearch(searchQuery)

    # Used to retrieve posts about target from all available social media websites.
    def retrievePosts(query):
        parsedQuery = util.Utilities.parseQuery(query)
        # search string used in the address bar to perform search.
        postsLink_1 = 'https://www.social-searcher.com/social-buzz/?q5=' + parsedQuery
        postsLink_2 = 'https://www.social-searcher.com/google-social-search/?q=' + parsedQuery + '&fb=on&tw=on&gp=on&in=on&li=on&pi=on'
        # returns a web page as a result of this search.
        print(postsLink_1)
        print(postsLink_2)
        print()
