import unittest
from sum_mixed_array import sum_mix

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(sum_mix([100, 50, 2]), 152)
    	self.assertEqual(sum_mix([50, "19", 1]), 70)
    	self.assertEqual(sum_mix(["433", "123", "0"]), 556)
    	

if __name__ == '__main__':
	unittest.main()