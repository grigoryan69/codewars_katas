import unittest
from count_by_x import count_by

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(count_by([2, 5], 3), [[2, 5], [2, 5, 2, 5], [2, 5, 2, 5, 2, 5]])
    	self.assertEqual(count_by([10, 5], 1), [[10, 5]])
    	self.assertEqual(count_by([6, 1], 2), [[6, 1], [6, 1, 6, 1]])
    	

if __name__ == '__main__':
	unittest.main()