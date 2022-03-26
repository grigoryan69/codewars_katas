import unittest
from basic_mathematical_operations import basic_op

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(basic_op('+', 5, 5), 10)
    	self.assertEqual(basic_op('-', 1616, 165), 1451)
    	self.assertEqual(basic_op('/', 56, 1.5), 37.333333333333336)
    	self.assertEqual(basic_op('*', 52, -5), -260)
    	

if __name__ == '__main__':
	unittest.main()