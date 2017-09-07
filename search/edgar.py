# This class performs a search in the website www.sec.gov that has confidential information about companies.
__startString__ = 0


# Provides a link to search in www.sec.gov.
def edgarSearch(query):
    # search string used in the address bar to perform search.
    query = _edgarSpace(query)
    edgarLink = 'https://www.sec.gov/cgi-bin/browse-edgar?company=' + _edgarParse(query) + '&owner=exclude&action=getcompany'
    # returns a web page as a result of this search.
    print(edgarLink)
    print()


# Removes space and adds the plus sign to complete the query.
def _edgarSpace(query):
    numSpaces = str(query).count(' ')
    return str(query).replace(' ', '+', numSpaces)


# Parses the query by cutting the -e flag.
def _edgarParse(query):
    flagIndex = str(query).index('-')
    query = query[__startString__:flagIndex]
    return query
