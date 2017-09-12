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
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://who.is/whois/www.abc.com')

    # tests if whois search is returning back the correct link for big flag.
    def test_whoIs_longFlag(self):
        query = "www.abc.com --whois"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.whoIsSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://who.is/whois/www.abc.com')

    # tests if whois search is returning back the correct link for single flag.
    def test_scanSearch_shortFlag(self):
        query = "www.abc.com -sc"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.scanSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://asafaweb.com/Scan?Url=www.abc.com')

    # tests if whois search is returning back the correct link for big flag.
    def test_scanSearch_longFlag(self):
        query = "www.abc.com --scan"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.scanSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://asafaweb.com/Scan?Url=www.abc.com')

    # tests if whois search is returning back the correct link for single flag.
    def test_archSearch_shortFlag(self):
        query = "www.abc.com -ar"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.archiveSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://web.archive.org/web/*/www.abc.com')

    # tests if whois search is returning back the correct link for big flag.
    def test_archSearch_longFlag(self):
        query = "www.abc.com --archive"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.archiveSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://web.archive.org/web/*/www.abc.com')

    # tests if whois search is returning back the correct link for single flag.
    def test_robotsView_shortFlag(self):
        query = "www.abc.com -rb"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.robotsView(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.abc.com/robots.txt')

    # tests if whois search is returning back the correct link for big flag.
    def test_robotsView_longFlag(self):
        query = "www.abc.com --robots"
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.robotsView(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.abc.com/robots.txt')

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
