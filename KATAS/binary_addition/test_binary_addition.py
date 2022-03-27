import unittest
from binary_addition import add_binary


class TestCodewarsCases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(add_binary(1, 1), '10')
        self.assertEqual(add_binary(3, 2), '101')
        self.assertEqual(add_binary(5, 5), '1010')
        self.assertEqual(add_binary(10, 10), '10100')


if __name__ == '__main__':
    unittest.main()
