import unittest
from remove_first_and_last_character import remove_char

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(remove_char('david'), 'avi')
    	self.assertEqual(remove_char('grigoryan'), 'rigorya')
    	self.assertEqual(remove_char('dav'), 'a')
    	

if __name__ == '__main__':
	unittest.main()