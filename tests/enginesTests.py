from unittest import TestCase
import search.engines as engines
import sys
from contextlib import contextmanager
from io import StringIO


class TestEngines(TestCase):

    # tests if search is returning back the correct link for two terms.
    def test_piplSearch_doubleWord(self):
        query = "john lennon -p"
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon')

    # tests if search is giving back correct link for three or more terms.
    def test_piplSearch_moreThanTwoWords(self):
        query = "dr john lennon -p"
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=dr+john+lennon')

    # tests if search for location is giving back correct link for single word location.
    def test_piplSearchLocation_singleWordLocation(self):
        query = "john lennon -p madrid -l"
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearchLocation(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon&l=madrid')

    # tests if search for location is giving back correct link for single word location.
    def test_piplSearchLocation_doubleWordLocation(self):
        query = "john lennon -p new york -l"
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearchLocation(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon&l=new+york')

    # tests searching using the long flag.
    def test_piplSearch_LongTerm(self):
        query = "john lennon --pipl"
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon')

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
