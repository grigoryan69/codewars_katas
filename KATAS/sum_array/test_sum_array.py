import unittest
from sum_array import sum_array

class TestCodewarsCases(unittest.TestCase):
    def test_case(self):
        self.assertEqual(sum_array([1231, 21, 2]), 1254)
        

if __name__ == '__main__':
    unittest.main()