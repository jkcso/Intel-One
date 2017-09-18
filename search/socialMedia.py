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
    __PINTEREST__ = "www.pinterest.com\n"
    __TUMBLR__ = "www.tumblr.com\n"
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

        elif media == 'pn':
            newQuery += SocialMedia.__PINTEREST__

        elif media == 'tb':
            newQuery += SocialMedia.__TUMBLR__

        elif media == 're':
            newQuery += SocialMedia.__REDDIT__

        searchQuery = engines.SearchEngines(newQuery)
        return engines.SearchEngines.googleSearch(searchQuery)

    # Used to retrieve posts on real time about target from all available social media websites.
    def realTimeSocialMediaSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        rtLink_0 = 'http://socialmention.com/search?q=' + parsedQuery + '&t=all&btnG=Search'
        rtLink_1 = 'https://www.social-searcher.com/social-buzz/?q5=' + parsedQuery
        rtLink_2 = 'https://www.social-searcher.com/google-social-search/?q=' + parsedQuery + '&fb=on&tw=on&gp=on&in=on&li=on&pi=on'
        rtLink_3 = 'https://app.buzzsumo.com/research/most-shared?type=articles&result_type=total&num_days=365&general_article&infographic&video&guest_post&giveaway&interview&q=' + parsedQuery + '&page=1'
        rtLink_4 = 'http://www.hashatit.com/hashtags/' + parsedQuery
        rtLink_5 = 'http://howsociable.com/' + parsedQuery
        rtLink_6 = 'http://www.uvrx.com/results-social/index.html?cx=008219812513279254587%3Ao2g7x-v-esw&cof=FORID%3A9&ie=UTF-8&q=' + parsedQuery
        print(rtLink_0)
        print(rtLink_1)
        print(rtLink_2)
        print(rtLink_3)
        print(rtLink_4)
        print(rtLink_5)
        print(rtLink_6)
        print()

    # Uses reddit username to get insights on lifetime reddit activity.
    def retrieveRedditUserStats(self):
        redditLink = 'https://snoopsnoo.com/u/' + util.Utilities.parseQuery(self.getQuery)
        print(redditLink)
        print()

    # searches about individuals in github, specifically about their projects.
    def sourceCodeSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        scLink = 'https://nerdydata.com/search?query=' + parsedQuery
        githubLink = 'https://github.com/search?q=' + parsedQuery
        print(scLink)
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

        print("Real time social media search:")
        self.realTimeSocialMediaSearch()

        print("Facebook search:")
        self.retrieveAccounts('fb')

        print("Linkedin search:")
        self.retrieveAccounts('ln')

        print("Twitter search:")
        self.retrieveAccounts('tw')

        print("Instagram search:")
        self.retrieveAccounts('in')

        print("Pinterest search:")
        self.retrieveAccounts('pn')

        print("Youtube search:")
        self.youtubeSearch()

        print("Tumblr search:")
        self.retrieveAccounts('tb')

        print("Source code search:")
        self.sourceCodeSearch()

        print("Reddit search:")
        self.retrieveAccounts('re')

        print("If victim target is reddit user, use the following as well:")
        self.retrieveRedditUserStats()
