import unittest
from sort_numbers import solution


class TestCodewarsCases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(solution([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(solution(None), [])


if __name__ == '__main__':
    unittest.main()
