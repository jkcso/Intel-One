from unittest import TestCase
import search.domains as domains
import sys
from contextlib import contextmanager
from io import StringIO


class TestDomains(TestCase):
    # tests if whois search is returning back the correct link for single flag.
    def test_whoIs_shortFlag(self):
        q = "www.abc.com -wh"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.whoIsSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://who.is/whois/www.abc.com')

    # tests if whois search is returning back the correct link for big flag.
    def test_whoIs_longFlag(self):
        q = "www.abc.com --whois"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.whoIsSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://who.is/whois/www.abc.com')

    # tests if dns search is returning back the correct link for single flag.
    def test_dns_shortFlag(self):
        q = "www.abc.com -dns"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.dnsLookup(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://mxtoolbox.com/SuperTool.aspx?action=a%3www.abc.com')

    # tests if dns search is returning back the correct link for single flag.
    def test_dns_longFlag(self):
        q = "www.abc.com --dnsLookup"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.dnsLookup(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://mxtoolbox.com/SuperTool.aspx?action=a%3www.abc.com')

    # tests if scan search is returning back the correct link for single flag.
    def test_scanSearch_shortFlag(self):
        q = "www.abc.com -sc"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.scanSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://asafaweb.com/Scan?Url=www.abc.com')

    # tests if scan search is returning back the correct link for big flag.
    def test_scanSearch_longFlag(self):
        q = "www.abc.com --scan"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.scanSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://asafaweb.com/Scan?Url=www.abc.com')

    # tests if archive search is returning back the correct link for single flag.
    def test_archSearch_shortFlag(self):
        q = "www.abc.com -ar"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.archiveSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://web.archive.org/web/www.abc.com')

    # tests if archive search is returning back the correct link for big flag.
    def test_archSearch_longFlag(self):
        q = "www.abc.com --archive"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.archiveSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://web.archive.org/web/www.abc.com')

    # tests if robots.txt search is returning back the correct link for single flag.
    def test_robotsView_shortFlag(self):
        q = "www.abc.com -rb"
        query = domains.Domains(q)
        with TestDomains.captured_output(self) as (out, err):
            domains.Domains.robotsView(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.abc.com/robots.txt')

    # tests if robots.txt search is returning back the correct link for big flag.
    def test_robotsView_longFlag(self):
        q = "www.abc.com --robots"
        query = domains.Domains(q)
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
