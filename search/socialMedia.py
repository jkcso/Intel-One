import search.engines as engines
import search.utilities as util
import search.query as qu


# Class responsible for social media account collection of target user, company or domain.
class SocialMedia(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Advanced google dork used for returning results including the provided url.
    __INURL__ = " inurl:\""

    # Social media websites that are currently supported by Who-Dis.
    __FACEBOOK__ = "www.facebook.com\""
    __LINKEDIN__ = "www.linkedin.com\""
    __TWITTER__ = "www.twitter.com\""
    __INSTAGRAM__ = "www.instagram.com\""
    __REDDIT__ = "www.reddit.com\""

    # Performs social search through google using the advanced google dork inurl.
    def retrieveAccounts(self, media):
        # Parses the query to avoid the flag inclusion while performing google search.
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        newQuery = parsedQuery + SocialMedia.__INURL__

        # Searches in corresponding social media indicated by user.
        if media == 'fb':
            newQuery += SocialMedia.__FACEBOOK__

        elif media == 'ln':
            newQuery += SocialMedia.__LINKEDIN__

        elif media == 'tw':
            newQuery += SocialMedia.__TWITTER__

        elif media == 'in':
            newQuery += SocialMedia.__INSTAGRAM__

        elif media == 're':
            newQuery += SocialMedia.__REDDIT__

        searchQuery = engines.SearchEngines(newQuery)
        return engines.SearchEngines.googleSearch(searchQuery)

    # Used to retrieve posts about target from all available social media websites.
    def retrievePosts(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        postsLink_1 = 'https://www.social-searcher.com/social-buzz/?q5=' + parsedQuery
        postsLink_2 = 'https://www.social-searcher.com/google-social-search/?q=' + parsedQuery + '&fb=on&tw=on&gp=on&in=on&li=on&pi=on'
        print(postsLink_1)
        print(postsLink_2)
        print()

    # Uses reddit username to get insights on lifetime reddit activity.
    def retrieveRedditUserStats(self):
        redditLink = 'https://snoopsnoo.com/u/' + util.Utilities.parseQuery(self.getQuery)
        print(redditLink)
        print()

    # searches about individuals in github, specifically about their projects.
    def githubSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        githubLink = 'https://github.com/search?q=' + parsedQuery
        print(githubLink)
        print()

    # searches youtube about specific user, individual or company.
    def youtubeSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        youtubeLink = 'https://www.youtube.com/user/' + parsedQuery
        print(youtubeLink)
        print()

    # Executes all of the above functions to perform social media search.
    def socialMediaAllSearches(self):
        print("\n---- SOCIAL MEDIA SEARCH ----")
        print("Facebook search:")
        self.retrieveAccounts('fb')

        print("Linkedin search:")
        self.retrieveAccounts('ln')

        print("Twitter search:")
        self.retrieveAccounts('tw')

        print("Instagram search:")
        self.retrieveAccounts('in')

        print("Youtube search:")
        self.youtubeSearch()

        print("GitHub search:")
        self.githubSearch()

        print("Reddit search:")
        self.retrieveAccounts('re')

        print("If victim target is reddit user, use the following as well:")
        self.retrieveRedditUserStats()

        print("Social media posts search:")
        self.retrievePosts()
