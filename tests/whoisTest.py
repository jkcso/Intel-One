from unittest import TestCase
import search.domains as whois
import sys
from contextlib import contextmanager
from io import StringIO


class TestWhoIs(TestCase):
    # tests if query parsing is done properly.
    def test_whoIsParse(self):
        query = "www.abc.com -w"
        parsed_query = whois._whoIsParse(query)
        self.assertEqual('www.abc.com ', parsed_query)

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

    # tests if whois search is returning back the correct link for single flag.
    def test_edgarSearch_singleDashFlag(self):
        query = "www.abc.com -w"
        with TestWhoIs.captured_output(self) as (out, err):
            whois.whoIsSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://who.is/whois/www.abc.com')

    # tests if whois search is returning back the correct link for big flag.
    def test_edgarSearch_doubleDashFlag(self):
        query = "www.abc.com --whois"
        with TestWhoIs.captured_output(self) as (out, err):
            whois.whoIsSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://who.is/whois/www.abc.com')
