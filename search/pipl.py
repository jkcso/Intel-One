# This class performs a search in the website www.pipl.com.  The reasoning behind this addition is that by
# social media search, we can't capture ALL the social media out there, but www.pipl.com will return all accounts
# related with the individual or website we are searching for no matter how old these accounts are.
startString = 0
MAX_SPACES = 1
PIPL_FLAG1 = '-p'


# Performs a search in www.pipl.com to capture the social media not captured above. Location is optional.
def piplSearch(query, location=None):
    # search string used in the address bar to perform search.
    query = piplSpace(query)
    piplLink = 'https://pipl.com/search/?q=' + piplParse(query)
    if location:
        # what is added to perform location search.
        # TODO locationSearch = '&l=' + location
        # TODO piplLink += locationSearch
        pass
        # return a web page as a result of this search.
    print(piplLink)


# Removes space and adds the plus sign to complete the query.
def piplSpace(query):
    return str(query).replace(' ', '+', MAX_SPACES)


# Parses the query by cutting the -p flag.
def piplParse(query):
    queryLength = len(query)
    effectiveLength = queryLength - len(PIPL_FLAG1)
    query = query[startString:effectiveLength]
    return query
