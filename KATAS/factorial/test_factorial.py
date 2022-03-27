import unittest
from factorial import factorial


class TestCodewarsCases(unittest.TestCase):
    def test_cases_positive(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(11), 39916800)
        self.assertEqual(factorial(12), 479001600)

    def test_cases_negative(self):
        with self.assertRaises(ValueError):
            factorial(13)
            print('ok')
        with self.assertRaises(ValueError):
            factorial(-1)
            print('ok')


if __name__ == '__main__':
    unittest.main()
