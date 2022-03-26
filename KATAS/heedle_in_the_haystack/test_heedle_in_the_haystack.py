import unittest
from heedle_in_the_haystack import find_needle

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(find_needle(['hay', 'junk', 'hay', 'hay',
    								'moreJunk', 'needle', 
    								'randomJunk']), 'found the needle at position 5')
    	

if __name__ == '__main__':
	unittest.main()