from unittest import TestCase
import search.engines as engines
import sys
from contextlib import contextmanager
from io import StringIO


class TestEngines(TestCase):

    # tests if duck duck go search is returning back the correct link for short flag.
    def test_ddGo_shortFlag(self):
        q = "glovdi -ddg"
        query = engines.SearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.SearchEngines.ddGoSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://duckduckgo.com/?q=glovdi')

    # tests if duck duck go search is returning back the correct link for long flag.
    def test_ddGo_longFlag(self):
        q = "glovdi -ddGo"
        query = engines.SearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.SearchEngines.ddGoSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://duckduckgo.com/?q=glovdi')

    # tests if baidu search is returning back the correct link for short flag.
    def test_baidu_shortFlag(self):
        q = "glovdi -bd"
        query = engines.SearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.SearchEngines.baiduSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=glovdi')

    # tests if baidu search is returning back the correct link for long flag.
    def test_baidu_longFlag(self):
        q = "glovdi --baidu"
        query = engines.SearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.SearchEngines.baiduSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=glovdi')

    # tests if baidu search is returning back the correct link for short flag.
    def test_bing_shortFlag(self):
        q = "glovdi -bg"
        query = engines.SearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.SearchEngines.bingSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.bing.com/search?q=glovdi')

    # tests if baidu search is returning back the correct link for long flag.
    def test_bing_longFlag(self):
        q = "glovdi --bing"
        query = engines.SearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.SearchEngines.bingSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.bing.com/search?q=glovdi')

    # tests if search is returning back the correct link for two terms.
    def test_piplSearch_doubleTerm_shortFlag(self):
        q = "john lennon -p"
        query = engines.PeopleSearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon')

    # tests if search is giving back correct link for three or more terms.
    def test_piplSearch_moreThanTwoWords_shortFlag(self):
        q = "dr john lennon -p"
        query = engines.PeopleSearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=dr+john+lennon')

    # tests if search for location is giving back correct link for single word location.
    def test_piplSearchLocation_singleLocation(self):
        q = "john lennon -p madrid -l"
        query = engines.PeopleSearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearchLocation(query, '-p')
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon&l=+madrid')

    # tests if search for location is giving back correct link for single word location.
    def test_piplSearchLocation_doubleLocation(self):
        q = "john lennon -p new york -l"
        query = engines.PeopleSearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearchLocation(query, '-p')
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon&l=+new+york')

    # tests searching using the long flag.
    def test_piplSearch_LongFlag(self):
        q = "john lennon --pipl"
        query = engines.PeopleSearchEngines(q)
        with TestEngines.captured_output(self) as (out, err):
            engines.PeopleSearchEngines.piplSearch(query)
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://pipl.com/search/?q=john+lennon')

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
