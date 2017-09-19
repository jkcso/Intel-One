from unittest import TestCase
import search.companies as companies
import sys
from contextlib import contextmanager
from io import StringIO


class TestCompanies(TestCase):

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
