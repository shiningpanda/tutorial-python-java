#-*- coding: utf-8 -*-
import unittest

import pysample

class PySampleTestCase(unittest.TestCase):
    
    def test(self):
        self.assertTrue(pysample.main())
    
if __name__ == '__main__':
    unittest.main()