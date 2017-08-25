# Does an initial google search about domain or individual
from google import search

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
    for result in search(query, tld=__TLD__, num=__NUM_RESULTS__, stop=__STOP__, pause=__PAUSE__):
        print(result)
