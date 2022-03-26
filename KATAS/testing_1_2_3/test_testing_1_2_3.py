import unittest
from testing_1_2_3 import number

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(number([]), [])
    	self.assertEqual(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])
    	self.assertEqual(number(["a", '', "b", "c", '', 'd']), \
    		['1: a', '2: ', '3: b', '4: c', '5: ', '6: d'])
 

if __name__ == '__main__':
	unittest.main()