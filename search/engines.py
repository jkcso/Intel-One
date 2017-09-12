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

    # returns duckduckgo searhable link.
    def ddGoSearch(query):
        parsedQuery = util.Utilities.parseQuery(query)
        ddGoLink = 'https://duckduckgo.com/?q=' + parsedQuery
        print(ddGoLink)
        print()

    # returns a baidu searchable link.
    def baiduSearch(query):
        parsedQuery = util.Utilities.parseQuery(query)
        baiduLink = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' + parsedQuery
        print(baiduLink)
        print()

    # returns a link in bing search engine to search.
    def bingSearch(query):
        parsedQuery = util.Utilities.parseQuery(query)
        bingLink = 'https://www.bing.com/search?q=' + parsedQuery
        print(bingLink)
        print()


# Class responsible for people search engines' search.
class PeopleSearchEngines(object):

    # Performs a search in www.pipl.com to capture the social media not captured above.
    def piplSearch(query):
        parsedQuery = util.Utilities.parseQuery(query)
        piplLink = 'https://pipl.com/search/?q=' + parsedQuery
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
