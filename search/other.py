import search.utilities as util


# A collection of functions that are not directly related to OSINT collection.
class Other(object):

    # Performs a search in www.who.is to capture information about a target domain.
    def shodanSearch(query):
        shodanLink = 'https://www.shodan.io/search?query=' + util.Utilities.parseQuery(query)
        print(shodanLink)
        print()
