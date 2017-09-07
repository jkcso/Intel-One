import search.utilities as util


# A collection of functions that are not directly related to OSINT collection.
class Other(object):

    # Performs a search in www.who.is to capture information about a target domain.
    def shodanSearch(query):
        # search string used in the address bar to perform search.
        shodanLink = 'https://www.shodan.io/search?query=' + util.Utilities.parseQuery(query)
        # returns a web page as a result of this search.
        print(shodanLink)
        print()
