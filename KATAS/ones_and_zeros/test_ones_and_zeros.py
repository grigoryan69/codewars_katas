import unittest
from ones_and_zeros import binary_array_to_number

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(binary_array_to_number([0,0,0,1]), 1)
    	self.assertEqual(binary_array_to_number([0,1,0,1]), 5)
    	self.assertEqual(binary_array_to_number([1,0,1,0]), 10)
    	self.assertEqual(binary_array_to_number([1,0,1,1]), 11)
 
 
if __name__ == '__main__':
	unittest.main()