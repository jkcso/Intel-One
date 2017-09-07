from unittest import TestCase
import search.companies as edgar
import sys
from contextlib import contextmanager
from io import StringIO


class TestEdgar(TestCase):
    # tests if query parsing is done properly.
    def test_edgarParse(self):
        query = "facebook -e"
        parsed_query = edgar._edgarParse(query)
        self.assertEqual('facebook ', parsed_query)

    # tests if space is replaced by '+' sign without parsing it.
    def test_edgarSpace(self):
        query = "facebook -e"
        new_query = edgar._edgarSpace(query)
        self.assertEqual('facebook+-e', new_query)

    # tests if space is replaced by '+' sign and parses it to retrieve query.
    def test_edgarSpace_plusParsed(self):
        query = "goldman sachs -e"
        new_query = edgar._edgarSpace(query)
        new_parsed_query = edgar._edgarParse(new_query)
        self.assertEqual('goldman+sachs+', new_parsed_query)

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
    def test_edgarSearch_singleTerm(self):
        query = "google -e"
        with TestEdgar.captured_output(self) as (out, err):
            edgar.edgarSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=google+&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_doubleTerm(self):
        query = "goldman sachs -e"
        with TestEdgar.captured_output(self) as (out, err):
            edgar.edgarSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=goldman+sachs+&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_singleTerm_fullFlag(self):
        query = "google --edgar"
        with TestEdgar.captured_output(self) as (out, err):
            edgar.edgarSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=google+&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_doubleTerm_fullFlag(self):
        query = "goldman sachs --edgar"
        with TestEdgar.captured_output(self) as (out, err):
            edgar.edgarSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=goldman+sachs+&owner=exclude&action=getcompany')
