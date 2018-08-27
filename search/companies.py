import search.utilities as util
import search.query as qu
import webbrowser


# Class including functions for OSINT collection for companies.
class Companies(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Provides a searchable link in corporation wiki for the target company queried.
    def companySearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        edgarLink = 'https://www.sec.gov/cgi-bin/browse-edgar?company=' + parsedQuery + '&owner=exclude&action=getcompany'
        cwLink = 'https://www.corporationwiki.com/search/results?term=' + parsedQuery
        hoovers = 'http://www.hoovers.com/company-information/company-search.html?term=' + parsedQuery
        glassdoor = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=microsoft&sc.keyword=' + parsedQuery + '&locT=&locId=&jobType='
        canLink = 'https://www.canada.ca/en/sr.html?cdn=canada&st=s&num=10&langs=en&st1rt=1&s5bm3ts21rch=x&q=' + parsedQuery
        wiki = 'https://en.wikipedia.org/wiki/' + parsedQuery
        marketVisual = 'http://www.marketvisual.com/Search/Results?searchString=' + parsedQuery
        opencorp = 'https://opencorporates.com/companies?jurisdiction_code=&q=' + parsedQuery
        serpstat = 'https://serpstat.com/keywords/?query=' + parsedQuery
        globalEdge = 'https://globaledge.msu.edu/search?q=' + parsedQuery
        comparablyLink = 'https://www.comparably.com/search?q=' + parsedQuery
        semrush = 'https://www.semrush.com/info/' + parsedQuery
        qLink = 'http://www.corporateinformation.com/Company-Search.aspx?s=' + parsedQuery
        ezilon = 'https://find.ezilon.com/search.php?q=' + parsedQuery + '&v=&x=0&y=0&f=1'
        owler = 'https://www.owler.com/iaApp/143891/' + parsedQuery
        ispionage = 'https://www.ispionage.com/freeaccountv2.aspx?q=' + parsedQuery
        ebr = 'http://www.ebr.org/?s=' + parsedQuery

        print(edgarLink)
        print(cwLink)
        print(hoovers)
        print(glassdoor)
        print(globalEdge)
        print(wiki)
        print(canLink)
        print(comparablyLink)
        print(opencorp)
        print(serpstat)
        print(semrush)
        print(qLink)
        print(ezilon)
        print(ispionage)
        print(owler)
        print(marketVisual)
        print(ebr)
        print()

        webbrowser.open(edgarLink)
        webbrowser.open(cwLink)
        webbrowser.open(hoovers)
        webbrowser.open(glassdoor)
        webbrowser.open(canLink)
        webbrowser.open(comparablyLink)
        webbrowser.open(opencorp)
        webbrowser.open(serpstat)
        webbrowser.open(semrush)
        webbrowser.open(qLink)
        webbrowser.open(ezilon)
        webbrowser.open(ispionage)
        webbrowser.open(owler)
        webbrowser.open(marketVisual)
        webbrowser.open(ebr)

    # Gets the email ending of the company.
    def getCompanyEmailFormat(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        ceLink = 'https://email-format.com/i/search_result/?q=' + parsedQuery
        print(ceLink)
        print()
        webbrowser.open(ceLink)

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

        webbrowser.open(postsLink_1)
        webbrowser.open(postsLink_2)
        webbrowser.open(postsLink_3)
        webbrowser.open(postsLink_4)
        webbrowser.open(postsLink_5)
        webbrowser.open(postsLink_6)

    # Executes all of the above functions to perform company search.
    def companyAllSearches(self):
        print("\n---- COMPANY RECORDS ----")

        print("Company information and search results can be found here:")
        self.companySearch()

        print("Annual reports, presentations and PDFs can be found here:")
        self.annualReportSearch()

        print("Email format of the company: ")
        self.getCompanyEmailFormat()
