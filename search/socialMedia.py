# Searches in for accounts in specific social media *through google* (at least for now).
# Facebook's url.
import search.google as google

FACEBOOK = "www.facebook.com"


# performs facebook search for the given query.
def facebookSearch(query):
    query += " inurl:" + "\"" + FACEBOOK + "\""
    return google.googleSearch(query)
