# Uses reddit username to get insights on lifetime reddit activity.
__startString__ = 0


# Performs a search in www.who.is to capture information about a target domain.
def redditSearch(query):
    # search string used in the address bar to perform search.
    redditLink = 'https://snoopsnoo.com/u/' + _redditParse(query)
    # returns a web page as a result of this search.
    print(redditLink)


# Parses the query by cutting the -p flag.
def _redditParse(query):
    flagIndex = str(query).index('-') or str(query).index('--')
    query = query[__startString__:flagIndex]
    return query
