import unittest
from convert_string_to_number import string_to_number

class TestCodewarsCases(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(string_to_number('100'), 100)
    	

if __name__ == '__main__':
	unittest.main()