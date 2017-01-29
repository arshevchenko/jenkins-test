#!/usr/bin/env python

import unittest
from jenkinstest import *

class TestJenkinsFunc(unittest.TestCase):
    def test_work(self):
        self.assertEqual(jenkins_test(), 5)

if __name__ == '__main__':
    unittest.main()
