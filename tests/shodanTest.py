from unittest import TestCase
import search.other as shodan
import sys
from contextlib import contextmanager
from io import StringIO


class TestShodan(TestCase):
    # tests if query parsing is done properly.
    def test_shodanParse(self):
        query = "zanussi -sh"
        parsed_query = shodan._shodanParse(query)
        self.assertEqual('zanussi ', parsed_query)

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

    # tests if shodan search is returning back the correct link for single flag.
    def test_edgarSearch_singleDashFlag(self):
        query = "zanussi -sh"
        with TestShodan.captured_output(self) as (out, err):
            shodan.shodanSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.shodan.io/search?query=zanussi')

    # tests if whois search is returning back the correct link for big flag.
    def test_edgarSearch_doubleDashFlag(self):
        query = "zanussi --shodan"
        with TestShodan.captured_output(self) as (out, err):
            shodan.shodanSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.shodan.io/search?query=zanussi')
