from unittest import TestCase
import search.reddit as reddit
import sys
from contextlib import contextmanager
from io import StringIO


class TestReddit(TestCase):
    # tests if query parsing is done properly.
    def test_redditParseShortFlag(self):
        query = "edgar -reU"
        parsed_query = reddit._redditParse(query)
        self.assertEqual('edgar ', parsed_query)

    # tests if query parsing is done properly.
    def test_redditParseLongFlag(self):
        query = "edgar --reditUser"
        parsed_query = reddit._redditParse(query)
        self.assertEqual('edgar ', parsed_query)

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

    # tests if reddit search is returning back the correct link for single flag.
    def test_redditSearch_singleDashFlag(self):
        query = "edgar -reU"
        with TestReddit.captured_output(self) as (out, err):
            reddit.redditSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://snoopsnoo.com/u/edgar')

    # tests if reddit search is returning back the correct link for big flag.
    def test_redditSearch_doubleDashFlag(self):
        query = "edgar --redditUser"
        with TestReddit.captured_output(self) as (out, err):
            reddit.redditSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://snoopsnoo.com/u/edgar')
