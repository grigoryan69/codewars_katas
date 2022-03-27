import unittest
from find_the_smallest_integer_in_the_array import find_smallest_int as finder

class TestCodewarsCases(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(finder([34, 15, 88, 2]), 2)
    	self.assertEqual(finder([23, 21, -4]), -4)
    	self.assertEqual(finder([6, 9, 3]), 3)
    	

if __name__ == '__main__':
	unittest.main()