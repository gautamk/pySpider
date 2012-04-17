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

    def tearDown(self):
        return 


suite = unittest.TestLoader().loadTestsFromTestCase(PySpiderTest)
unittest.TextTestRunner(verbosity=2).run(suite)