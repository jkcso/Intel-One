import search.utilities as util


# Class including functions for OSINT collection for companies.
class Companies(object):

    # Provides a link to search in www.sec.gov.
    def edgarSearch(query):
        # search string used in the address bar to perform search.
        parsedQuery = util.Utilities.parseQuery(query)
        edgarLink = 'https://www.sec.gov/cgi-bin/browse-edgar?company=' + parsedQuery + '&owner=exclude&action=getcompany'
        # returns a web page as a result of this search.
        print(edgarLink)
        print()

    # Provides a searchable link in corporation wiki for the target company queried.
    def corpWikiSearch(query):
        parsedQuery = util.Utilities.parseQuery(query)
        cwLink = 'https://www.corporationwiki.com/search/results?term=' + parsedQuery
        print(cwLink)
        print()

    # Provides link to annual reports, slideshows and other insights of a company.
    def annualReportSearch(query):
        parsedQuery = util.Utilities.parseQuery(query)
        postsLink_1 = 'http://www.annualreports.com/Companies?search=' + parsedQuery
        postsLink_2 = 'https://www.reportlinker.com/report/search/keywords/' + parsedQuery
        print(postsLink_1)
        print(postsLink_2)
        print()
