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

    # Provides link to annual reports, slideshows and other insights of a company.
    def annualReportSearch(query):
        parsedQuery = util.Utilities.parseQuery(query)
        # search string used in the address bar to perform search.
        postsLink_1 = 'http://www.annualreports.com/Companies?search=' + parsedQuery
        postsLink_2 = 'https://www.reportlinker.com/report/search/keywords/' + parsedQuery
        # returns a web page as a result of this search.
        print(postsLink_1)
        print(postsLink_2)
        print()
