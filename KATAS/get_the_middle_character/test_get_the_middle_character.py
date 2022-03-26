import unittest
from get_the_middle_character import get_middle

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(get_middle('abcd'), 'bc')
    	self.assertEqual(get_middle('david'), 'v')
 

if __name__ == '__main__':
	unittest.main()