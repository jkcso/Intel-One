# This class performs a search in the website www.pipl.com.  The reasoning behind this addition is that by
# social media search, we can't capture ALL the social media out there, but www.pipl.com will return all accounts
# related with the individual or website we are searching for no matter how old these accounts are.
__startString__ = 0
__PIPL_FLAG1__ = ' -p'


# Performs a search in www.pipl.com to capture the social media not captured above.
def piplSearch(query):
    # search string used in the address bar to perform search.
    query = _piplSpace(query)
    piplLink = 'https://pipl.com/search/?q=' + _piplParse(query)
    # returns a web page as a result of this search.
    print(piplLink)


# This function performs search to the optional location in www.pipl.com.
def piplSearchLocation(query):
    location = _piplLocation(query)
    query = _piplParseLocation(query)
    query = _piplSpace(query)
    piplLink = 'https://pipl.com/search/?q=' + query + '&l=' + location
    print(piplLink)


# Removes space and adds the plus sign to complete the query.
def _piplSpace(query):
    numSpaces = str(query).count(' ')
    return str(query).replace(' ', '+', numSpaces)


# Parses the query by cutting the -p flag.
def _piplParse(query):
    queryLength = len(query)
    effectiveLength = queryLength - len(__PIPL_FLAG1__)
    query = query[__startString__:effectiveLength]
    return query


# Parses query including location.
def _piplParseLocation(query):
    flagIndex = str(query).index('-p')
    query = query[__startString__:flagIndex]
    return query


# Parses the query to return the location by splitting it.
def _piplLocation(query):
    first = '-p '
    last = ' -l'
    try:
        start = query.index(first) + len(first)
        end = query.index(last, start)
        return query[start:end]
    except ValueError:
        return ""
