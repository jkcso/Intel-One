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
