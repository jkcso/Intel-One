import search.utilities as util
import search.query as qu
import webbrowser


# Class including functions for OSINT collection for target domains.
class Domains(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Performs search in who.is records giving information about a target domain.
    def whoIsSearch(self):
        # search string used in the address bar to perform search.
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        pageGlimpse = 'http://www.pageglimpse.com/' + parsedQuery
        whoIsLink_0 = 'https://who.is/whois/' + parsedQuery
        whoIsLink_1 = 'http://www.dnsstuff.com/tools#whois|type=domain&&value=' + parsedQuery
        whoIsLink_2 = 'http://domainbigdata.com/' + parsedQuery
        whoIsLink_3 = 'http://www.domaincrawler.com/' + parsedQuery
        whoIsLink_4 = 'http://www.domainhistory.net/' + parsedQuery
        whoIsLink_5 = 'http://whois.domaintools.com/' + parsedQuery
        whoIsLink_6 = 'https://app2.follow.net/#domains/' + parsedQuery
        whoIsLink_7 = 'https://majestic.com/reports/site-explorer?q=' + parsedQuery + '&oq=' + parsedQuery + '&IndexDataSource=F'
        whoIsLink_8 = 'https://www.robtex.com/dns-lookup/' + parsedQuery
        whoIsLink_9 = 'http://www.whoishostingthis.com/?q=' + parsedQuery

        # returns a web page as a result of this search.
        print(whoIsLink_5)
        print(whoIsLink_0)
        print(whoIsLink_1)
        print(whoIsLink_9)
        print(whoIsLink_2)
        print(whoIsLink_3)
        print(whoIsLink_4)
        print(whoIsLink_7)
        print(whoIsLink_6)
        print(whoIsLink_8)
        print(pageGlimpse)
        print()

        webbrowser.open(whoIsLink_5)
        webbrowser.open(whoIsLink_0)
        webbrowser.open(whoIsLink_1)
        webbrowser.open(whoIsLink_9)
        webbrowser.open(whoIsLink_2)
        webbrowser.open(whoIsLink_3)
        webbrowser.open(whoIsLink_4)
        webbrowser.open(whoIsLink_7)
        webbrowser.open(whoIsLink_6)
        webbrowser.open(whoIsLink_8)
        webbrowser.open(pageGlimpse)

    # Performs search in who.is records giving information about a target domain.
    def dnsLookup(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        dnsLookupLink_0 = 'https://mxtoolbox.com/SuperTool.aspx?action=a%3' + parsedQuery
        dedicatedOrNot = parsedQuery + '.dedicatedornot.com'
        netcraft = 'http://toolbar.netcraft.com/site_report?url=' + parsedQuery + '#last_reboot'
        dnsLookupLink_1 = 'http://dnshistory.org/dns-records/' + parsedQuery
        dnsLookupLink_2 = 'http://www.dnsstuff.com/tools#dnsReport|type=domain&&value=' + parsedQuery
        dnsLookupLink_3 = 'http://research.dnstrails.com/tools/lookup.htm?domain=' + parsedQuery
        dnsLookupLink_4 = 'http://dnsviz.net/d/' + parsedQuery + '/analyze/'
        dnsLookupLink_5 = 'https://intodns.com/' + parsedQuery
        dnsLookupLink_6 = 'https://mxtoolbox.com/SuperTool.aspx?action=mx%3a' + parsedQuery + '&run=toolpage'
        dnsLookupLink_7 = 'http://sameid.net/id/' + parsedQuery + '/'
        dnsLookupLink_8 = 'https://www.tcpiputils.com/search?q=' + parsedQuery
        dnsLookupLink_9 = 'http://dnssec-debugger.verisignlabs.com/' + parsedQuery

        print(dnsLookupLink_0)
        print(dedicatedOrNot)
        print(netcraft)
        print(dnsLookupLink_1)
        print(dnsLookupLink_2)
        print(dnsLookupLink_9)
        print(dnsLookupLink_8)
        print(dnsLookupLink_3)
        print(dnsLookupLink_6)
        print(dnsLookupLink_4)
        print(dnsLookupLink_5)
        print(dnsLookupLink_7)
        print()

        webbrowser.open(dnsLookupLink_0)
        webbrowser.open(dedicatedOrNot)
        webbrowser.open(netcraft)
        webbrowser.open(dnsLookupLink_1)
        webbrowser.open(dnsLookupLink_2)
        webbrowser.open(dnsLookupLink_9)
        webbrowser.open(dnsLookupLink_8)
        webbrowser.open(dnsLookupLink_3)
        webbrowser.open(dnsLookupLink_6)
        webbrowser.open(dnsLookupLink_4)
        webbrowser.open(dnsLookupLink_5)
        webbrowser.open(dnsLookupLink_7)

    # Retrieves a link for scanning a target domain.
    def scanSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        scanLink = 'https://asafaweb.com/Scan?Url=' + parsedQuery
        print(scanLink)
        print()
        webbrowser.open(scanLink)

    # Retrieves a link into archived version of target domain
    def archiveSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        archiveLink = 'https://web.archive.org/web/' + parsedQuery  # TODO an issue with star.
        googleCache = 'http://webcache.googleusercontent.com/search?q=cache:http://' + parsedQuery + '/'
        webCache = 'http://webcache.googleusercontent.com/search?q=cache:' + parsedQuery
        screenShot = 'http://www.screenshots.com/' + parsedQuery + '/'
        print(archiveLink)
        print(googleCache)
        print(webCache)
        print(screenShot)
        print()

        webbrowser.open(archiveLink)
        webbrowser.open(googleCache)
        webbrowser.open(webCache)
        webbrowser.open(screenShot)

    # Retrieves a link into archived version of target domain
    def builtWith(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        buildWithLink = 'https://builtwith.com/' + parsedQuery
        print(buildWithLink)
        print()
        webbrowser.open(buildWithLink)

    # Provides the link to view the robots.txt file of a target domain.
    # This function has as a precondition that was is queries is a valid link.
    def robotsView(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        newQuery = 'https://' + str(parsedQuery) + '/robots.txt'
        print(newQuery)
        print()
        webbrowser.open(newQuery)

    # Executes all of the above functions.
    def domainAllSearches(self):
        print("\n---- DOMAIN INFO ----")

        print("View official whois records:")
        self.whoIsSearch()

        print("View results from DNS lookup:")
        self.dnsLookup()

        print("View archived versions of the website:")
        self.archiveSearch()

        print("Technologies and tools used to built the website:")
        self.builtWith()

        print("View the robots.txt file with disallowed resource access:")
        self.robotsView()

        print("Scan the domain for common vulnerabilities here:")
        self.scanSearch()
