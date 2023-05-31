import unittest
from add import add
class TestCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(20,30),50)
        self.assertAlmostEqual(add(10,21),31)
        
    def test_values(self):
        self.assertTrue(add(0,0.1))
        self.assertIs(add(1,1),add(1,1))
        self.assertIsNot(add(1,1),add(1,1))
        # self.assertRaises(ValueError,add,'vinesh','kumar')
        # self.assertRaises(ValueError,add,'vinesh',10)s
        # self.assertRaises(ValueError,add,'vinesh',True)
        # self.assertRaises(ValueError,add,True,False)
        # self.assertRaises(ValueError,add,12.3,12)