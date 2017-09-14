# Created to be used as the parent class of all classes.  Ideally this is the class where all classes in the search
# directory will inherit from.  This way the code will be neater and more readable.


class Query(object):
    def __init__(self, query):
        self.__query = str(query)

    # The getter method
    @property
    def getQuery(self):
        return self.__query
