# This class performs a search in the website www.pipl.com.  The reasoning behind this addition is that by
# social media search, we can't capture ALL the social media out there, but www.pipl.com will return all accounts
# related with the individual or website we are searching for no matter how old these accounts are.
startString = 0
PIPL_FLAG1 = '-p'


# Performs a search in www.pipl.com to capture the social media not captured above.
def piplSearch(query):
    # search string used in the address bar to perform search.
    query = piplSpace(query)
    piplLink = 'https://pipl.com/search/?q=' + piplParse(query)
    # returns a web page as a result of this search.
    print(piplLink)


# This function performs search to the optional location in www.pipl.com.
def piplSearchLocation(query):
    location = piplLocation(query)
    print(location)

# Removes space and adds the plus sign to complete the query.
def piplSpace(query):
    numSpaces = str(query).count(' ')
    return str(query).replace(' ', '+', numSpaces)


# Parses the query by cutting the -p flag.
def piplParse(query):
    queryLength = len(query)
    effectiveLength = queryLength - len(PIPL_FLAG1)
    query = query[startString:effectiveLength]
    return query


# Parses the query to return the location by splitting it.
def piplLocation(query):
    first = '-p '
    last = ' -l'
    try:
        start = query.index(first) + len(first)
        end = query.index(last, start)
        return query[start:end]
    except ValueError:
        return ""
