import unittest
from disemvowel_trolls import disemvowel

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(disemvowel('david'), 'dvd')
    	self.assertEqual(disemvowel('LOL'), 'LL')
    	self.assertEqual(disemvowel('a'), '')
    	

if __name__ == '__main__':
	unittest.main()