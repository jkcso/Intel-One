from unittest import TestCase
import search.pipl as pipl
import sys
from contextlib import contextmanager
from io import StringIO


class TestPipl(TestCase):
    # tests if method extracts the given single word location correctly.
    def test_piplLocation_singleWord(self):
        query = "john lennon -p madrid -l"
        location = pipl._piplLocation(query)
        self.assertEqual('madrid', location)

    # tests if method extracts the given single word location correctly.
    def test_piplLocation_doubleWord(self):
        query = "john lennon -p new york -l"
        location = pipl._piplLocation(query)
        self.assertEqual('new york', location)

    # tests if query is parsed correctly before -p flag.
    def test_piplParseLocation(self):
        query = "john lennon -p new york -l"
        parsed_query = pipl._piplParseLocation(query)
        self.assertEqual('john lennon', parsed_query)

    # tests if query parsing is done properly.
    def test_piplParse(self):
        query = "john lennon -p"
        parsed_query = pipl._piplParse(query)
        self.assertEqual('john lennon', parsed_query)

    # tests if space is replaced by '+' sign without parsing it.
    def test_piplSpace(self):
        query = "john lennon -p"
        new_query = pipl._piplSpace(query)
        self.assertEqual('john+lennon+-p', new_query)

    # tests if space is replaced by '+' sign and parses it to retrieve query.
    def test_piplSpace_plusParsed(self):
        query = "john lennon -p"
        new_query = pipl._piplSpace(query)
        new_parsed_query = pipl._piplParse(new_query)
        self.assertEqual('john+lennon', new_parsed_query)

    # tests output in screen.
    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    # tests if search is returning back the correct link for two terms.
    def test_piplSearch_doubleWord(self):
        query = "john lennon -p"
        with TestPipl.captured_output(self) as (out, err):
            pipl.piplSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon')

    # tests if search is giving back correct link for three or more terms.
    def test_piplSearch_moreThanTwoWords(self):
        query = "dr john lennon -p"
        with TestPipl.captured_output(self) as (out, err):
            pipl.piplSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=dr+john+lennon')

    # tests if search for location is giving back correct link for single word location.
    def test_piplSearchLocation_singleWordLocation(self):
        query = "john lennon -p madrid -l"
        with TestPipl.captured_output(self) as (out, err):
            pipl.piplSearchLocation(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon&l=madrid')

    # tests if search for location is giving back correct link for single word location.
    def test_piplSearchLocation_doubleWordLocation(self):
        # TODO fix this
        pass
