import search.utilities as util


# Class responsible for OSINT collection against companies.
class Companies(object):

    # Provides a link to search in www.sec.gov.
    def edgarSearch(query):
        # search string used in the address bar to perform search.
        parsedQuery = util.Utilities.parseQuery(query)
        edgarLink = 'https://www.sec.gov/cgi-bin/browse-edgar?company=' + parsedQuery + '&owner=exclude&action=getcompany'
        # returns a web page as a result of this search.
        print(edgarLink)
        print()
