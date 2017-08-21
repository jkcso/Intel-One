# Searches in for accounts in specific social media *through google* (at least for now).
# Facebook's url.
import search.google as google

FACEBOOK = "www.facebook.com"
LINKEDIN = "www.linkedin.com"


# performs facebook search for the given query.
def facebookSearch(query):
    query += " inurl:" + "\"" + FACEBOOK + "\""
    return google.googleSearch(query)


# performs linkedin search for the given query.
def linkedinSearch(query):
    query += " inurl:" + "\"" + LINKEDIN + "\""
    return google.googleSearch(query)
