import search.utilities as util
import search.query as qu


# Class including functions for OSINT collection for target domains.
class Domains(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Performs search in who.is records giving information about a target domain.
    def whoIsSearch(self):
        # search string used in the address bar to perform search.
        whoIsLink = 'https://who.is/whois/' + util.Utilities.parseQuery(self.getQuery)
        # returns a web page as a result of this search.
        print(whoIsLink)
        print()

    # Retrieves a link for scanning a target domain.
    def scanSearch(self):
        scanLink = 'https://asafaweb.com/Scan?Url=' + util.Utilities.parseQuery(self.getQuery)
        print(scanLink)
        print()

    # Retrieves a link into archived version of target domain
    def archiveSearch(self):
        archiveLink = 'https://web.archive.org/web/*/' + util.Utilities.parseQuery(self.getQuery)
        print(archiveLink)
        print()

    # Provides the link to view the robots.txt file of a target domain.
    # This function has as a precondition that was is queries is a valid link.
    def robotsView(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        newQuery = 'https://' + str(parsedQuery) + '/robots.txt'
        print(newQuery)
        print()
