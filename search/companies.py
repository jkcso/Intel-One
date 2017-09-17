import search.utilities as util
import search.query as qu


# Class including functions for OSINT collection for companies.
class Companies(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Provides a link to search in www.sec.gov.
    def edgarSearch(self):
        # search string used in the address bar to perform search.
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        edgarLink = 'https://www.sec.gov/cgi-bin/browse-edgar?company=' + parsedQuery + '&owner=exclude&action=getcompany'
        # returns a web page as a result of this search.
        print(edgarLink)
        print()

    # Provides a searchable link in corporation wiki for the target company queried.
    def corpWikiSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        cwLink = 'https://www.corporationwiki.com/search/results?term=' + parsedQuery
        print(cwLink)
        print()

    # Provides link to annual reports, slideshows and other insights of a company.
    def annualReportSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        postsLink_1 = 'http://www.annualreports.com/Companies?search=' + parsedQuery
        postsLink_2 = 'https://www.reportlinker.com/report/search/keywords/' + parsedQuery
        postsLink_3 = 'http://www.authorstream.com/tag/' + parsedQuery
        postsLink_4 = 'http://www.freefullpdf.com/#gsc.tab=0&gsc.q=' + parsedQuery
        postsLink_5 = 'https://offshoreleaks.icij.org/search?utf8=✓&q=' + parsedQuery
        postsLink_6 = 'https://www.slideshare.net/search/slideshow?searchfrom=header&q=' + parsedQuery
        print(postsLink_1)
        print(postsLink_2)
        print(postsLink_3)
        print(postsLink_4)
        print(postsLink_5)
        print(postsLink_6)
        print()

    # Executes all of the above functions to perform company search.
    def companyAllSearches(self):
        print("\n---- COMPANY RECORDS ----")

        print("Government records found using the edgar search engine:")
        self.edgarSearch()

        print("Corporation info can be found here:")
        self.corpWikiSearch()

        print("Annual reports, presentations and PDFs can be found here:")
        self.annualReportSearch()
