import unittest
from find_the_stray_number import stray


class TestCodewarsCases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(stray([1, 1, 3]), 3)
        self.assertEqual(stray([1, 99, 9, 1]), 99)
        self.assertEqual(stray([9, 9, 9]), None)


if __name__ == '__main__':
    unittest.main()
