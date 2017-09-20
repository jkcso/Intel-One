from google import search
import search.utilities as util
import search.query as qu


# Class including functions for OSINT collection using search engines.
class SearchEngines(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Top level domain search
    __TLD__ = "com"
    # Number of results we want back
    __NUM_RESULTS__ = 8
    # Last result to retrieve.  Use none if you want to search forever.
    __STOP__ = 1
    # Lapse to wait between HTTP requests.
    __PAUSE__ = 2

    # returns google search results.
    def googleSearch(self):
        for result in search(self.getQuery, tld=SearchEngines.__TLD__, num=SearchEngines.__NUM_RESULTS__,
                             stop=SearchEngines.__STOP__, pause=SearchEngines.__PAUSE__):
            print(result)
        print()

    # returns duckduckgo searhable link.
    def ddGoSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        ddGoLink = 'https://duckduckgo.com/?q=' + parsedQuery
        print(ddGoLink)
        print()

    # returns a baidu searchable link.
    def baiduSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        baiduLink = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' + parsedQuery
        print(baiduLink)
        print()

    # returns a link in bing search engine to search.
    def bingSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        bingLink = 'https://www.bing.com/search?q=' + parsedQuery
        print(bingLink)
        print()

    # returns a link in excite search engine to search - specifically news, latest posts about queries -.
    def exciteNewsSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        exciteNewsLink = 'http://msxml.excite.com/search/news?q=' + parsedQuery + '&fcoid=411&fcop=left&om_nextpage=True&fpid=2'
        print(exciteNewsLink)
        print()

    # returns a link in fact bites search engine to search very old posts about search term.
    def oldArticlesSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        oldArticlesLink = 'http://www.factbites.com/topics/' + parsedQuery
        print(oldArticlesLink)
        print()

    # returns a link in qwant search engine collecting search, media, and social.
    def qwantSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        qwantLink = 'https://www.qwant.com/?q=' + parsedQuery + '&t=all'
        print(qwantLink)
        print()

    # returns a link in clustering websites that provide search to many places.
    def clusteringSearchEngines(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        carrotLink = 'http://search.carrot2.org/stable/search?source=web&view=folders&skin=fancy-compact&query=' + parsedQuery
        cluzLink = 'http://www.cluuz.com/Default.aspx?list=y&yahoo=y&q=' + parsedQuery
        print(carrotLink)
        print(cluzLink)
        print()

    # search engine used to match keywords.
    def keywordMatching(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        kmLink = 'http://www.keywordspy.com/research/search.aspx?q=' + parsedQuery + '&type=domains'
        qrLink = 'https://keywordtool.io/search/google/10371113?keyword=' + parsedQuery + '&country=&language=en#suggestions'
        wolrdTracker = 'https://www.wordtracker.com/search?query=' + parsedQuery
        exLink = 'http://www.onelook.com/reverse-dictionary.shtml?s=' + parsedQuery
        print(kmLink)
        print(qrLink)
        print(wolrdTracker)
        print(exLink)
        print()

    # searches RSS feeds
    def searchRSS(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        rssLink_0 = 'https://www.rsssearchhub.com/feeds?q=' + parsedQuery
        rssLink_1 = 'http://fetchrss.com/generator/invalid?url=' + parsedQuery
        print(rssLink_0)
        print(rssLink_1)
        print()

    # Executes all of the above functions.
    def searchEngineAllSearches(self):
        print("\n---- SEARCH ENGINES ----")

        print("Google search:")
        self.googleSearch()

        print("DuckDuckGo search:")
        self.ddGoSearch()

        print("Baidu search:")
        self.baiduSearch()

        print("Bing search:")
        self.bingSearch()

        print("Qwant search:")
        self.qwantSearch()

        print("Clustering multi search:")
        self.clusteringSearchEngines()

        print("Keyword matching search:")
        self.keywordMatching()

        print("Excite news search:")
        self.exciteNewsSearch()

        print("Fact bites news search:")
        self.oldArticlesSearch()

        print("Search in RSS Feeds:")
        self.searchRSS()


# Class responsible for people search engines' search.
class PeopleSearchEngines(SearchEngines):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Performs a search in www.pipl.com to capture the social media not captured above.
    def peopleSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        parse411 = self.__411parse__()
        peekParse = self._peekParse__()

        piplLink = 'https://pipl.com/search/?q=' + parsedQuery
        canadaLink = 'http://www.canada411.ca/search/?stype=si&what=' + parsedQuery
        forebears = 'http://forebears.io/place-search?q=' + parsedQuery
        infospace = 'http://search.infospace.com/search/web?q=' + parsedQuery + '&searchbtn=Search'
        intermentSearch = 'http://www.interment.net/data/search-general.htm?cx=partner-pub-1928517298809652%3A6045987309&cof=FORID%3A10&ie=ISO-8859-1&q=' + parsedQuery + '&sa=Search'
        marketVisual = 'http://www.marketvisual.com/Search/Results?searchString=' + parsedQuery
        nationalArchives = 'http://discovery.nationalarchives.gov.uk/results/r?_q=' + parsedQuery
        link411Website = 'http://www.411.com/name/' + parse411
        whitePages = 'http://www.whitepages.com/name/' + parse411
        spokeo = 'https://www.spokeo.com/' + parse411
        thatsThem = 'https://thatsthem.com/name/' + parse411
        peekLink = 'http://www.peekyou.com/' + peekParse
        yasni = 'http://www.yasni.com/' + parsedQuery + '/check+people?sh'
        zabasaSearch = 'http://www.zabasearch.com/people/' + parsedQuery + '/'
        journal = 'https://network.expertisefinder.com/searchexperts?query=' + parsedQuery
        wink = 'https://www.wink.com/people/?pf=&nm=' + parsedQuery

        print(piplLink)
        print(peekLink)
        print(canadaLink)
        print(link411Website)
        print(whitePages)
        print(forebears)
        print(infospace)
        print(intermentSearch)
        print(marketVisual)
        print(nationalArchives)
        print(spokeo)
        print(thatsThem)
        print(yasni)
        print(zabasaSearch)
        print(journal)
        print(wink)
        print()

    # This function performs search to the optional location in www.pipl.com.
    def piplSearchLocation(self, flag):
        parsedLocation = PeopleSearchEngines.__parseLocation__(self, flag)
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        piplLink = 'https://pipl.com/search/?q=' + parsedQuery + '&l=' + parsedLocation
        print(piplLink)
        print()

    # Executes all of the above functions.
    def peopleEngineAllSearches(self):
        print("\n---- PEOPLE SEARCH ENGINES ----")

        print("Note: We suggest to add a location to make your search more specific.")
        print("To do so, please use: <name> -i <location> -l")
        print("\nSearch links in multiple people search engines:")
        self.peopleSearch()

        print("Search in pipl search engine with location:")
        self.piplSearchLocation('-i')

    # Parses the query to return the location by splitting it.
    def __parseLocation__(self, flag):
        first = str(flag)
        last = ' -l'
        try:
            stringQuery = self.getQuery
            start = stringQuery.index(first) + len(first)
            end = stringQuery.index(last, start)
            parsedQuery = self.getQuery[start:end]
            subQuery = util.Utilities.substituteSpaces(parsedQuery)
            return subQuery
        except ValueError:
            return ""

    # 411 People search website has a very unique matching of keywords using '-'.
    def __411parse__(self):
        q = util.Utilities.parseQuery(self.getQuery)
        numSpaces = self.getQuery.count(' ')
        return q.replace('+', '-', numSpaces)

    def _peekParse__(self):
        q = util.Utilities.parseQuery(self.getQuery)
        numSpaces = self.getQuery.count(' ')
        return q.replace('+', '_', numSpaces)


# Class responsible for email validity.
class EmailValidityEngine(SearchEngines):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # This function performs search to the optional location in www.pipl.com.
    def emailValidity(self):
        evLink_0 = 'https://mailjagger.ga/api/validate/' + self.getQuery
        evLink_1 = 'http://www.reversegenie.com/email_search/' + self.getQuery
        revLookup = 'https://thatsthem.com/email/' + self.getQuery
        print(evLink_0)
        print(evLink_1)
        print("Reverse email lookup:")
        print(revLookup)
        print()

    # Performs email and social media search on given email.
    def emailSearch(self):
        print("\n---- EMAIL VALIDITY ----")

        print("Checks email validity:")
        self.emailValidity()
