class Utilities(object):

    # Flags intro used by the user to indicate an action.
    __SH_FLAG__ = '-'
    __LO_FLAG__ = '--'

    # Uses social searcher website collecting posts on given keyword on all social media.
    __startString__ = 0
    # The length of the space character, used to remove trailing space at the end of parsing keyword.
    __spaceCharLength__ = 1

    # Parses the query to avoid the flag inclusion while performing google search.
    def parseQuery(query):
        flagIndex = str(query).index(Utilities.__SH_FLAG__) or str(query).index(Utilities.__LO_FLAG__)
        parsedQuery = query[Utilities.__startString__:flagIndex - Utilities.__spaceCharLength__]
        return parsedQuery
