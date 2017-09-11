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
