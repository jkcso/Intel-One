import search.utilities as util


# This class is responsible for all functions having to do with target domains.
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
        # search string used in the address bar to perform search.
        scanLink = 'https://asafaweb.com/Scan?Url=' + util.Utilities.parseQuery(query)
        # returns a web page as a result of this search.
        print(scanLink)
        print()
