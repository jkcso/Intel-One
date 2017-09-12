import search.utilities as util


# Class including functions for OSINT collection for target domains.
class Domains(object):

    # Performs search in who.is records giving information about a target domain.
    def whoIsSearch(query):
        # search string used in the address bar to perform search.
        whoIsLink = 'https://who.is/whois/' + util.Utilities.parseQuery(query)
        # returns a web page as a result of this search.
        print(whoIsLink)
        print()

    # Retrieves a link for scanning a target domain.
    def scanSearch(query):
        scanLink = 'https://asafaweb.com/Scan?Url=' + util.Utilities.parseQuery(query)
        print(scanLink)
        print()

    # Retrieves a link into archived version of target domain
    def archiveSearch(query):
        archiveLink = 'https://web.archive.org/web/*/' + util.Utilities.parseQuery(query)
        print(archiveLink)
        print()

    # Provides the link to view the robots.txt file of a target domain.
    # This function has as a precondition that was is queries is a valid link.
    def robotsView(query):
        parsedQuery = util.Utilities.parseQuery(query)
        newQuery = 'https://' + str(parsedQuery) + '/robots.txt'
        print(newQuery)
        print()
