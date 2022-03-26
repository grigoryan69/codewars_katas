import unittest
from count_of_positives_sum_of_negatives import count_positives_sum_negatives

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(count_positives_sum_negatives([100]), [1, 0])
    	self.assertEqual(count_positives_sum_negatives([1, 6, 20]), [3, 0])
    	self.assertEqual(count_positives_sum_negatives([5, 3, -22]), [2, -22])
    	

if __name__ == '__main__':
	unittest.main()