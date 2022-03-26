import unittest
from will_you_make_it import zero_fuel

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(zero_fuel(100, 50, 2), True)
    	self.assertEqual(zero_fuel(50, 19, 1), False)
    	self.assertEqual(zero_fuel(433, 123, 0), False)
    	

if __name__ == '__main__':
	unittest.main()