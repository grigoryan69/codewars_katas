import unittest
from can_we_divide_it import is_divide_by

class TestCodewarsCases(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(is_divide_by(-12, 2, -6), True)
    	self.assertEqual(is_divide_by(45, 5, 15), True)
    	self.assertEqual(is_divide_by(-12, 2, -5), False)
    	self.assertEqual(is_divide_by(45, 1, 6), False)
    	

if __name__ == '__main__':
	unittest.main()