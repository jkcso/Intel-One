from unittest import TestCase
import search.domains as domains
import sys
from contextlib import contextmanager
from io import StringIO


class TestDomains(TestCase):
    # tests if whois search is returning back the correct link for single flag.
    def test_whoIs_shortFlag(self):
        query = "www.abc.com -wh"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.whoIsSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://who.is/whois/www.abc.com')

    # tests if whois search is returning back the correct link for big flag.
    def test_whoIs_LongFlag(self):
        query = "www.abc.com --whois"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.whoIsSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://who.is/whois/www.abc.com')

    # tests if whois search is returning back the correct link for single flag.
    def test_scanSearch_shortFlag(self):
        query = "www.abc.com -sc"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.scanSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://asafaweb.com/Scan?Url=www.abc.com')

    # tests if whois search is returning back the correct link for big flag.
    def test_edgarSearch_LongFlag(self):
        query = "www.abc.com --scan"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.scanSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://asafaweb.com/Scan?Url=www.abc.com')

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
