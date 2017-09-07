import search.utilities as util
from unittest import TestCase


class TestUtilities(TestCase):
    # tests if query parsing is done properly with short flag.
    def test_parseQuery_shortFlag(self):
        query = "www.abc.com -flag"
        parsedQuery = util.Utilities.parseQuery(query)
        self.assertEqual('www.abc.com', parsedQuery)

    # tests if query parsing is done properly with long flag.
    def test_parseQuery_longFlag(self):
        query = "www.abc.com --flag"
        parsedQuery = util.Utilities.parseQuery(query)
        self.assertEqual('www.abc.com', parsedQuery)

    def test_substituteSpaces_oneSpace(self):
        query = "abc def"
        parsedQuery = util.Utilities.substituteSpaces(query)
        self.assertEqual('abc+def', parsedQuery)

    def test_substituteSpaces_multiSpace(self):
        query = "abc def "
        parsedQuery = util.Utilities.substituteSpaces(query)
        self.assertEqual('abc+def+', parsedQuery)

