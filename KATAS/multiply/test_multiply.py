import unittest
from multiply import multiply

class TestFindShort(unittest.TestCase):
    def test_case(self):
    	self.assertEqual(multiply(160, 5), 800)
    	

if __name__ == '__main__':
	unittest.main()