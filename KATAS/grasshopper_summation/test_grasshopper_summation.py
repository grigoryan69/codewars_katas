import unittest
from grasshopper_summation import summation

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(summation(100), 5050)
    	self.assertEqual(summation(6), 21)
    	self.assertEqual(summation(2), 3)
    	

if __name__ == '__main__':
	unittest.main()