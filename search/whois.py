# This class is responsible for performing search in who.is website giving information about a target domain.
# indicates the starting index in a string.
__startString__ = 0


# Performs a search in www.who.is to capture information about a target domain.
def whoIsSearch(query):
    # search string used in the address bar to perform search.
    whoIsLink = 'https://who.is/whois/' + _whoIsParse(query)
    # returns a web page as a result of this search.
    print(whoIsLink)
    print()


# Parses the query by cutting the -p flag.
def _whoIsParse(query):
    flagIndex = str(query).index('-') or str(query).index('--')
    query = query[__startString__:flagIndex]
    return query
