from google import search
import search.utilities as util


# Class including functions for OSINT collection using search engines.
class SearchEngines(object):

    # Top level domain search
    __TLD__ = "com"
    # Number of results we want back
    __NUM_RESULTS__ = 8
    # Last result to retrieve.  Use none if you want to search forever.
    __STOP__ = 1
    # Lapse to wait between HTTP requests.
    __PAUSE__ = 2

    # returns google search results.
    def googleSearch(query):
        for result in search(query, tld=SearchEngines.__TLD__, num=SearchEngines.__NUM_RESULTS__,
                             stop=SearchEngines.__STOP__, pause=SearchEngines.__PAUSE__):
            print(result)
        print()


# Class responsible for people search engines' search.
class PeopleSearchEngines(object):

    # Performs a search in www.pipl.com to capture the social media not captured above.
    def piplSearch(query):
        # search string used in the address bar to perform search.
        parsedQuery = util.Utilities.parseQuery(query)
        piplLink = 'https://pipl.com/search/?q=' + parsedQuery
        # returns a web page as a result of this search.
        print(piplLink)
        print()

    # This function performs search to the optional location in www.pipl.com.
    def piplSearchLocation(query):
        parsedLocation = PeopleSearchEngines.__parseLocation__(query)
        parsedQuery = util.Utilities.parseQuery(query)
        piplLink = 'https://pipl.com/search/?q=' + parsedQuery + '&l=' + parsedLocation
        print(piplLink)
        print()

    # Parses the query to return the location by splitting it.
    def __parseLocation__(query):
        first = '-p '
        last = ' -l'
        try:
            stringQuery = str(query)
            start = stringQuery.index(first) + len(first)
            end = stringQuery.index(last, start)
            parsedQuery = query[start:end]
            parsedQuery = util.Utilities.substituteSpaces(parsedQuery)
            return parsedQuery
        except ValueError:
            return ""
