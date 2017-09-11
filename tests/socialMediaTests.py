from unittest import TestCase
import search.socialMedia as sm
import sys
from contextlib import contextmanager
from io import StringIO


class TestSocialMedia(TestCase):
    # tests if socialSearcher search is returning back the correct link for single flag.
    def test_socialSearcherSearch_shortFlag(self):
        query = "edgar -ss"
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.retrievePosts(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.social-searcher.com/social-buzz/?q5=edgar\n'
                               'https://www.social-searcher.com/google-social-search/?q=edgar&fb=on&tw=on&gp=on&in=on&li=on&pi=on')

    # tests if socialSearcher search is returning back the correct link for big flag.
    def test_socialSearcherSearch_longFlag(self):
        query = "edgar --social"
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.retrievePosts(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.social-searcher.com/social-buzz/?q5=edgar\n'
                               'https://www.social-searcher.com/google-social-search/?q=edgar&fb=on&tw=on&gp=on&in=on&li=on&pi=on')

    # tests if reddit search is returning back the correct link for single flag.
    def test_redditSearch_shortFlag(self):
        query = "edgar -ure"
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.retrieveRedditUserStats(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://snoopsnoo.com/u/edgar')

    # tests if reddit search is returning back the correct link for big flag.
    def test_redditSearch_longFlag(self):
        query = "edgar --userReddit"
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.retrieveRedditUserStats(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://snoopsnoo.com/u/edgar')

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
