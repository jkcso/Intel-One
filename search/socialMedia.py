# imports the google wrapper class defined in this directory.
import search.google as google


# Responsible for social media account collection of target user, company or domain.
class SocialMedia(object):
    # Flags intro used by the user to indicate an action.
    __SH_FLAG__ = '-'
    __LO_FLAG__ = '--'

    # Advanced google dork used for returning results including the provided url.
    __INURL__ = " inurl:"

    # Social media websites that are currently supported by Who-Dis.
    __FACEBOOK__ = "www.facebook.com"
    __LINKEDIN__ = "www.linkedin.com"
    __TWITTER__ = "www.twitter.com"
    __INSTAGRAM__ = "www.instagram.com"
    __REDDIT__ = "www.reddit.com"

    # Uses social searcher website collecting posts on given keyword on all social media.
    __startString__ = 0
    # The length of the space character, used to remove trailing space at the end of parsing keyword.
    __spaceCharLength__ = 1

    # Parses the query to avoid the flag inclusion while performing google search.
    def __parseQuery(query):
        flagIndex = str(query).index(SocialMedia.__SH_FLAG__) or str(query).index(SocialMedia.__LO_FLAG__)
        parsedQuery = query[SocialMedia.__startString__:flagIndex - SocialMedia.__spaceCharLength__]
        return parsedQuery

    # Performs social search through google using the advanced google dork inurl.
    def retrieveAccounts(query, media):
        # Parses the query to avoid the flag inclusion while performing google search.
        parsedQuery = SocialMedia.__parseQuery(query)
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

        return google.googleSearch(query)

    # Used to retrieve posts about target from all available social media websites.
    # TODO needs the space function for name+surname form
    # def retrievePosts(query):
    #     parsedQuery = SocialMedia.__parseQuery(query)
    #     # search string used in the address bar to perform search.
    #     postsLink_1 = 'https://www.social-searcher.com/social-buzz/?q5=' + parsedQuery
    #     postsLink_2 = 'https://www.social-searcher.com/google-social-search/?q=' + parsedQuery + '&fb=on&tw=on&gp=on&in=on&li=on&pi=on'
    #     # returns a web page as a result of this search.
    #     print(postsLink_1)
    #     print(postsLink_2)
    #     print()
