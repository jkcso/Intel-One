# Library used to search in google.
from google import search


# Class responsible for search engine search.
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
    pass
