import random
import unittest

class PySpiderTest(unittest.TestCase):
    def setUp(self):
        return 

    def test_canary(self):
        self.assertEqual(1,1)

    def tearDown(self):
        return 


suite = unittest.TestLoader().loadTestsFromTestCase(PySpiderTest)
unittest.TextTestRunner(verbosity=2).run(suite)