from unittest import TestCase
import search.socialMedia as sm
import sys
from contextlib import contextmanager
from io import StringIO


class TestSocialSearcher(TestCase):
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

    # tests if socialSearcher search is returning back the correct link for single flag.
    def test_socialSearcherSearch_singleDashFlag(self):
        query = "edgar -ss"
        with TestSocialSearcher.captured_output(self) as (out, err):
            sm.SocialSearcher.ssSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.social-searcher.com/social-buzz/?q5=edgar\n'
                               'https://www.social-searcher.com/google-social-search/?q=edgar&fb=on&tw=on&gp=on&in=on&li=on&pi=on')

    # tests if socialSearcher search is returning back the correct link for big flag.
    def test_socialSearcherSearch_doubleDashFlag(self):
        query = "edgar --social"
        with TestSocialSearcher.captured_output(self) as (out, err):
            sm.SocialSearcher.ssSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.social-searcher.com/social-buzz/?q5=edgar\n'
                               'https://www.social-searcher.com/google-social-search/?q=edgar&fb=on&tw=on&gp=on&in=on&li=on&pi=on')