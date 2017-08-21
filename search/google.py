# Does an initial google search about domain or individual
from google import search

# Top level domain search
TLD = "com"
# Number of results we want back
NUM_RESULTS = 8
# Last result to retrieve.  Use none if you want to search forever.
STOP = 1
# Lapse to wait between HTTP requests.
PAUSE = 2


# returns google search results.
def googleSearch(query):
    for result in search(query, tld=TLD, num=NUM_RESULTS, stop=STOP, pause=PAUSE):
        print(result)
