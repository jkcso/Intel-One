# This class is responsible for performing search in shodan.io website giving information about a target domain.
# indicates the starting index in a string.
__startString__ = 0


# Performs a search in www.who.is to capture information about a target domain.
def shodanSearch(query):
    # search string used in the address bar to perform search.
    shodanLink = 'https://www.shodan.io/search?query=' + _shodanParse(query)
    # returns a web page as a result of this search.
    print(shodanLink)
    print()


# Parses the query by cutting the -p flag.
def _shodanParse(query):
    flagIndex = str(query).index('-') or str(query).index('--')
    query = query[__startString__:flagIndex]
    return query
