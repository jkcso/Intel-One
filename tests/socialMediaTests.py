from unittest import TestCase
import search.socialMedia as sm
import sys
from contextlib import contextmanager
from io import StringIO


class TestSocialMedia(TestCase):

    # tests if reddit search is returning back the correct link for single flag.
    def test_redditSearch_shortFlag(self):
        q = "edgar -ure"
        query = sm.SocialMedia(q)
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.retrieveRedditUserStats(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://snoopsnoo.com/u/edgar')

    # tests if reddit search is returning back the correct link for big flag.
    def test_redditSearch_longFlag(self):
        q = "edgar --userReddit"
        query = sm.SocialMedia(q)
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.retrieveRedditUserStats(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://snoopsnoo.com/u/edgar')

    # tests if reddit search is returning back the correct link for single flag.
    def test_sourceCodeSearch_shortFlag(self):
        q = "whodis -gh"
        query = sm.SocialMedia(q)
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.sourceCodeSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://nerdydata.com/search?query=whodis\n'
                               'https://github.com/search?q=whodis')

    # tests if reddit search is returning back the correct link for big flag.
    def test_githubSearch_longFlag(self):
        q = "whodis --github"
        query = sm.SocialMedia(q)
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.sourceCodeSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://nerdydata.com/search?query=whodis\n'
                               'https://github.com/search?q=whodis')

    # tests if reddit search is returning back the correct link for single flag.
    def test_youtubeSearch_shortFlag(self):
        q = "google -yt"
        query = sm.SocialMedia(q)
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.youtubeSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.youtube.com/user/google')

    # tests if reddit search is returning back the correct link for big flag.
    def test_youtubeSearch_longFlag(self):
        q = "google --youtube"
        query = sm.SocialMedia(q)
        with TestSocialMedia.captured_output(self) as (out, err):
            sm.SocialMedia.youtubeSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.youtube.com/user/google')

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
