# This class performs a search in the website www.pipl.com.  The reasoning behind this addition is that by
# social media search, we can't capture ALL the social media out there, but www.pipl.com will return all accounts
# related with the individual or website we are searching for no matter how old these accounts are.
# indicates the starting index in a string.
__startString__ = 0


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
    flagIndex = str(query).index('-') or str(query).index('--')
    query = query[__startString__:flagIndex]
    return query


# Parses query including location.
def _piplParseLocation(query):
    flagIndex = str(query).index('-')
    query = query[__startString__:flagIndex]
    return query


# Parses the query to return the location by splitting it.
def _piplLocation(query):
    first = '-p '
    last = ' -l'
    try:
        start = query.index(first) + len(first)
        end = query.index(last, start)
        query = query[start:end]
        return _piplSpace(query)
    except ValueError:
        return ""
