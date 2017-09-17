from unittest import TestCase
import search.companies as companies
import sys
from contextlib import contextmanager
from io import StringIO


class TestCompanies(TestCase):
    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_singleTerm_shortFlag(self):
        q = "google -ed"
        query = companies.Companies(q)
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.edgarSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=google&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_doubleTerm_shortFlag(self):
        q = "goldman sachs -ed"
        query = companies.Companies(q)
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.edgarSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=goldman+sachs&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_singleTerm_longFlag(self):
        q = "google --edgar"
        query = companies.Companies(q)
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.edgarSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=google&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_doubleTerm_longFlag(self):
        q = "goldman sachs --edgar"
        query = companies.Companies(q)
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.edgarSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=goldman+sachs&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_corpWikiSearch_shortFlag(self):
        q = "google -cw"
        query = companies.Companies(q)
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.corpWikiSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link,
                            'https://www.corporationwiki.com/search/results?term=google')

    # tests if search is returning back the correct link for two terms.
    def test_corpWikiSearch_longFlag(self):
        q = "google --corpWiki"
        query = companies.Companies(q)
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.corpWikiSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link,
                            'https://www.corporationwiki.com/search/results?term=google')

    # tests if search is returning back the correct link for two terms.
    def test_annualReportSearch_shortFlag(self):
        q = "natwest -are"
        query = companies.Companies(q)
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.annualReportSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'http://www.annualreports.com/Companies?search=natwest\n'
                               'https://www.reportlinker.com/report/search/keywords/natwest\n'
                               'http://www.authorstream.com/tag/natwest\n'
                               'http://www.freefullpdf.com/#gsc.tab=0&gsc.q=natwest\n'
                               'https://offshoreleaks.icij.org/search?utf8=✓&q=natwest\n'
                               'https://www.slideshare.net/search/slideshow?searchfrom=header&q=natwest')

    # tests if search is returning back the correct link for two terms.
    def test_annualReportSearch_longFlag(self):
        q = "natwest --reports"
        query = companies.Companies(q)
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.annualReportSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'http://www.annualreports.com/Companies?search=natwest\n'
                               'https://www.reportlinker.com/report/search/keywords/natwest\n'
                               'http://www.authorstream.com/tag/natwest\n'
                               'http://www.freefullpdf.com/#gsc.tab=0&gsc.q=natwest\n'
                               'https://offshoreleaks.icij.org/search?utf8=✓&q=natwest\n'
                               'https://www.slideshare.net/search/slideshow?searchfrom=header&q=natwest')

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
