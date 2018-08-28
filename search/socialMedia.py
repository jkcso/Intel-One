import search.engines as engines
import search.utilities as util
import search.query as qu
import webbrowser


# Class responsible for social media account collection of target user, company or domain.
class SocialMedia(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Advanced google dork used for returning results including the provided url.
    __INURL__ = "+site:"

    # Social media websites that are currently supported by our tool.
    __FACEBOOK__ = "facebook.com"
    __LINKEDIN__ = "linkedin.com"
    __TWITTER__ = "twitter.com"
    __INSTAGRAM__ = "instagram.com"
    __PINTEREST__ = "pinterest.com"
    __TUMBLR__ = "tumblr.com"
    __REDDIT__ = "reddit.com"

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
        searchQuery.TO_PARSE = False  # search query is ready to be passed without parse in search engines by now.
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
        webbrowser.open(rtLink_0)
        webbrowser.open(rtLink_1)
        webbrowser.open(rtLink_2)
        webbrowser.open(rtLink_3)
        webbrowser.open(rtLink_4)
        webbrowser.open(rtLink_5)
        webbrowser.open(rtLink_6)

    # Gets the tweets about the keyword queried.
    def retrieveTweets(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        tweetsLink_0 = 'https://twitter.com/search?q=' + parsedQuery + '&src=typd'
        tweetsLink_1 = 'http://backtweets.com/search/?q=' + parsedQuery
        tweetsLink_2 = 'https://socialbearing.com/search/user/' + parsedQuery
        tweetsLink_3 = 'http://twbirthday.com/' + parsedQuery + '/'
        print(tweetsLink_0)
        print(tweetsLink_1)
        print(tweetsLink_2)
        print("\nTrying to retrieve twitter user account birthday here:")
        print(tweetsLink_3)
        print()
        webbrowser.open(tweetsLink_0)
        webbrowser.open(tweetsLink_1)
        webbrowser.open(tweetsLink_2)
        webbrowser.open(tweetsLink_3)

    # Gets the instagram posts about specific keyword.
    def retrieveInstagramPosts(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        redditLink = 'http://hashtagify.me/hashtag/' + parsedQuery
        print(redditLink)
        print()
        webbrowser.open(redditLink)

    def retrieveTwitterAnalytics(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        twitterAnalyticsLink_1 = 'https://burrrd.com/analyze?username=' + parsedQuery
        twitterAnalyticsLink_2 = 'https://foller.me/' + parsedQuery
        twitterAnalyticsLink_3 = 'http://gettwitterid.com/?user_name=' + parsedQuery + '&submit=GET+USER+ID'
        twitterAnalyticsLink_4 = 'https://www.hashtags.org/analytics/' + parsedQuery + '/'
        print(twitterAnalyticsLink_1)
        print(twitterAnalyticsLink_2)
        print(twitterAnalyticsLink_3)
        print(twitterAnalyticsLink_4)
        print()
        webbrowser.open(twitterAnalyticsLink_1)
        webbrowser.open(twitterAnalyticsLink_2)
        webbrowser.open(twitterAnalyticsLink_3)
        webbrowser.open(twitterAnalyticsLink_4)

    # Gets the reddit posts about specific keyword.
    def retrieveRedditPosts(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        redditLink = 'http://metareddit.com/reddits/search/cloud/?query=' + parsedQuery
        print(redditLink)
        print()
        webbrowser.open(redditLink)

    # Uses reddit username to get insights on lifetime reddit activity.
    def retrieveRedditUserStats(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        redditLink_0 = 'https://snoopsnoo.com/u/' + parsedQuery
        redditLink_1 = 'https://atomiks.github.io/reddit-user-analyser/#' + parsedQuery
        redditLink_2 = 'http://redditmetrics.com/r/' + parsedQuery
        redditLink_3 = 'https://snoopsnoo.com/u/' + parsedQuery
        print(redditLink_0)
        print(redditLink_1)
        print(redditLink_2)
        print(redditLink_3)
        print()
        webbrowser.open(redditLink_0)
        webbrowser.open(redditLink_1)
        webbrowser.open(redditLink_2)
        webbrowser.open(redditLink_3)

    # searches about individuals in github, specifically about their projects.
    def sourceCodeSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        scLink = 'https://nerdydata.com/search?query=' + parsedQuery
        githubLink = 'https://github.com/search?q=' + parsedQuery
        print(scLink)
        print(githubLink)
        print()
        webbrowser.open(scLink)
        webbrowser.open(githubLink)

    # searches youtube about specific user, individual or company.
    def youtubeSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        youtubeLink = 'https://www.youtube.com/user/' + parsedQuery
        print(youtubeLink)
        print()
        webbrowser.open(youtubeLink)

    # searches videos on other video databases about specific user, individual or company.
    def otherVdieoSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        metacafeLink = 'http://www.metacafe.com/videos_about/' + parsedQuery + '/'
        metatube = 'http://www.metatube.com/en/videos/?q=' + parsedQuery
        aol = 'https://www.aol.com/video/search/?q=' + parsedQuery
        bing = 'https://www.bing.com/videos/search?q=' + parsedQuery + '&go=Submit&qs=n&form=QBLH&scope=video&sp=-1&pq=' + parsedQuery
        blinkx = 'http://www.blinkx.com/search/' + parsedQuery
        earthcam = 'http://www.earthcam.com/search/ft_search.php?term=' + parsedQuery
        geoSearch = 'http://www.geosearchtool.com/?q=&la=35.1327266&lo=33.31108219999999&lr=10km&tw=any&cl=&sl=' + parsedQuery
        archive = 'https://archive.org/details/opensource_movies?and[]=' + parsedQuery
        liveleak = 'https://www.liveleak.com/browse?q=' + parsedQuery
        veoh = 'http://www.veoh.com/find/?query=' + parsedQuery
        voxalead = 'http://voxalead.labs.exalead.com/search/?q=' + parsedQuery + '&lr=&r=&l=en'
        yahoo = 'http://video.search.yahoo.com/search/video;_ylt=AwrDQ2oPaMJZZysAGy36w8QF;_ylc=X1MDOTY3ODEzMDYEX3IDMgRiY2sDMjB2aGwxaGNraXJoaiUyNmIlM0QzJTI2cyUzRDkxBGZyAwRncHJpZAMEbXRlc3RpZANudWxsBG5fc3VnZwMwBG9yaWdpbgN2aWRlby5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzYEcXVlcnkDZ2xvdmRpBHRfc3RtcAMxNTA1OTEyOTUyBHZ0ZXN0aWQDbnVsbA--?pvid=mb7ibDEwLjEgfjUMWUluMwCeMjEzLgAAAACoVxVj&fr2=sb-top-video.search.yahoo.com&p=' + parsedQuery

        print(metacafeLink)
        print(metatube)
        print(aol)
        print(bing)
        print(blinkx)
        print(veoh)
        print(yahoo)
        print(earthcam)
        print(liveleak)
        print(voxalead)
        print(archive)
        print(geoSearch)
        print()
        webbrowser.open(metacafeLink)
        webbrowser.open(metatube)
        webbrowser.open(aol)
        webbrowser.open(bing)
        webbrowser.open(blinkx)
        webbrowser.open(veoh)
        webbrowser.open(yahoo)
        webbrowser.open(earthcam)
        webbrowser.open(liveleak)
        webbrowser.open(voxalead)
        webbrowser.open(archive)
        webbrowser.open(geoSearch)

    # searches in blogs about provided keyword.
    def blogSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        blogLink_0 = 'http://www.blogsearchengine.org/search.html?cx=partner-pub-9634067433254658%3A5laonibews6&cof=FORID%3A10&ie=ISO-8859-1&q=' + parsedQuery
        blogLink_1 = 'http://omgili.com/search?siteType=&q=' + parsedQuery
        print(blogLink_0)
        print(blogLink_1)
        print()
        webbrowser.open(blogLink_0)
        webbrowser.open(blogLink_1)

    # Executes all of the above functions to perform social media search.
    def socialMediaAllSearches(self):
        print("\n---- SOCIAL MEDIA SEARCH ----")

        print("Real time social media search:")
        self.realTimeSocialMediaSearch()

        print("Facebook search:")
        self.retrieveAccounts('fb')

        print("Linkedin search:")
        self.retrieveAccounts('ln')

        print("Browser plugin that finds emails of people's profiles in Linkedin.")
        print('https://chrome.google.com/webstore/detail/ftl/lkpekgkhmldknbcgjicjkomphkhhdkjj?hl=en-GB')

        print("\nTwitter search:")
        self.retrieveAccounts('tw')

        print("Tweets mentioning target keyword:")
        self.retrieveTweets()

        print("Specific username's twitter analytics:")
        self.retrieveTwitterAnalytics()

        print("Instagram search:")
        self.retrieveAccounts('in')

        print("Instagram posts mentioning target keyword:")
        self.retrieveInstagramPosts()

        print("Pinterest search:")
        self.retrieveAccounts('pn')

        print("Youtube search:")
        self.youtubeSearch()

        print("Other video database search:")
        self.otherVdieoSearch()

        print("Tumblr search:")
        self.retrieveAccounts('tb')

        print("Source code search:")
        self.sourceCodeSearch()

        print("Reddit search:")
        self.retrieveAccounts('re')

        print("Reddit posts mentioning target keyword:")
        self.retrieveRedditPosts()

        print("Stats and Analytics on specific reddit user:")
        self.retrieveRedditUserStats()

        print("Blog search on given keyword:")
        self.blogSearch()
