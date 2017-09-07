class Utilities(object):

    # Flags intro used by the user to indicate an action.
    __SH_FLAG__ = '-'
    __LO_FLAG__ = '--'

    # Uses social searcher website collecting posts on given keyword on all social media.
    __startString__ = 0
    # The length of the space character, used to remove trailing space at the end of parsing keyword.
    __spaceCharLength__ = 1
    # Maximum number of spaces allowed without proceeding into further parsing.
    __spaceMAX__ = 1

    # Parses the query to avoid the flag inclusion while performing google search.
    def parseQuery(query):
        flagIndex = str(query).index(Utilities.__SH_FLAG__) or str(query).index(Utilities.__LO_FLAG__)
        parsedQuery = query[Utilities.__startString__:flagIndex - Utilities.__spaceCharLength__]

        # Handles the cases where search terms are > 1 therefore we need to add a '+' in the position of each space.
        parsedQueryNumSpaces = str(query).count(' ')
        if parsedQueryNumSpaces > Utilities.__spaceMAX__:
            parsedQuery = Utilities.__removeSpaces__(parsedQuery)

        return parsedQuery

    # Removes space and adds the plus sign to complete the query.
    def __removeSpaces__(query):
        numSpaces = str(query).count(' ')
        return str(query).replace(' ', '+', numSpaces)
