import unittest
from shortest_word import find_short

class TestCodewarsCases(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(find_short('abcd ab dc'), 2)
    	self.assertEqual(find_short('abcd abs dcs'), 3)
    	self.assertEqual(find_short('david grigoryan'), 5)
    	self.assertEqual(find_short('one ,'), 0)
 

if __name__ == '__main__':
	unittest.main()