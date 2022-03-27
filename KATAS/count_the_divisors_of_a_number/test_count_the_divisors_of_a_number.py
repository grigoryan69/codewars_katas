import unittest
from count_the_divisors_of_a_number import divisors

class TestCodewarsCases(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(divisors(1), 1)
    	self.assertEqual(divisors(3), 2)
    	self.assertEqual(divisors(4), 3)
    	

if __name__ == '__main__':
	unittest.main()