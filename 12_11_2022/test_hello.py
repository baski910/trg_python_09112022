# Testrunner - script for writing test cases
# TestSuite - A class for writing test. This class will take unittest.TestCase as base class
# TestCase - methods of TestSuite. The methods name should begin with 'test'
import unittest
from hello import is_prime

class MyTestCase(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(19))

    def test_not_prime(self):
        self.assertFalse(is_prime(18))

if __name__ == '__main__':
    unittest.main()