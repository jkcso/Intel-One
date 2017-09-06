# Searches in for accounts in specific social media *through google* (at least for now).
# Facebook's url.
import search.google as google

__FACEBOOK__ = "www.facebook.com"
__LINKEDIN__ = "www.linkedin.com"
__TWITTER__ = "www.twitter.com"
__INSTAGRAM__ = "www.instagram.com"
__REDDIT__ = "www.reddit.com"


# performs facebook search for the given query.
def facebookSearch(query):
    query += " inurl:" + "\"" + __FACEBOOK__ + "\""
    return google.googleSearch(query)


# performs linkedin search for the given query.
def linkedinSearch(query):
    query += " inurl:" + "\"" + __LINKEDIN__ + "\""
    return google.googleSearch(query)


# performs twitter search for the given query.
def twitterSearch(query):
    query += " inurl:" + "\"" + __TWITTER__ + "\""
    return google.googleSearch(query)


# performs instagram search for the given query.
def instagramSearch(query):
    query += " inurl:" + "\"" + __INSTAGRAM__ + "\""
    return google.googleSearch(query)


# performs reddit search for the given query.
def redditSearch(query):
    query += " inurl:" + "\"" + __REDDIT__ + "\""
    return google.googleSearch(query)


# searches all social media at once returning recent posts about target.
class SocialSearcher:
    # Uses social searcher website collecting posts on given keyword on all social media.
    __startString__ = 0
    # The length of the space character, used to remove trailing space at the end of parsing keyword.
    __spaceCharLength__ = 1

    # Performs a search in www.who.is to capture information about a target domain.
    def ssSearch(query):
        # search string used in the address bar to perform search.
        ssLink_1 = 'https://www.social-searcher.com/social-buzz/?q5=' + SocialSearcher._ssParse(query)
        ssLink_2 = 'https://www.social-searcher.com/google-social-search/?q=' + SocialSearcher._ssParse(query) + '&fb=on&tw=on&gp=on&in=on&li=on&pi=on'
        # returns a web page as a result of this search.
        print(ssLink_1)
        print(ssLink_2)

    # Parses the query by cutting the -p flag.
    def _ssParse(query):
        flagIndex = str(query).index('-') or str(query).index('--')
        query = query[SocialSearcher.__startString__:flagIndex - SocialSearcher.__spaceCharLength__]
        return query
