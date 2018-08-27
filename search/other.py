import search.utilities as util
import search.query as qu
import webbrowser


# A collection of functions that are not directly related to OSINT collection.
class Other(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Performs a search in www.who.is to capture information about a target domain.
    def shodanSearch(self):
        shodanLink = 'https://www.shodan.io/search?query=' + util.Utilities.parseQuery(self.getQuery)
        print(shodanLink)
        print()
        webbrowser.open(shodanLink)
