#!/usr/bin/env python

import unittest
import jenkinstest

class TestJenkinsFunc(unittest.TestCase):
    def test_work():
        self.assertEqual(jenkins_test(), 5)

if __name__ == '__main__':
    unittest.main()
