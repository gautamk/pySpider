import random
import unittest
from pySpider import *

class PySpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = PySpider()
        return 

    def test_canary(self):
        self.assertEqual(1,1)

    def test_class(self):
        self.assertTrue(isinstance(self.spider,PySpider))

    def test_url_valid(self):
        self.assertFalse( self.spider.is_valid_url("/") )
        self.assertFalse( self.spider.is_valid_url("http://") )
        self.assertFalse( self.spider.is_valid_url("google.com") )
        self.assertFalse( self.spider.is_valid_url("www.google.com") )
        self.assertTrue(self.spider.is_valid_url("http://www.google.com") )
    
    def test_enqueue(self):
        url = "http://google.com"
        self.spider.enqueue(url)
        self.assertEqual(url,self.spider.repo[0])

    def test_dequeue(self):
        url = "http://google.com"
        self.spider.enqueue(url)
        self.assertEqual(url,self.spider.dequeue())

    def test_crawl:
        pass



    
    def tearDown(self):
        return 


suite = unittest.TestLoader().loadTestsFromTestCase(PySpiderTest)
unittest.TextTestRunner(verbosity=2).run(suite)