import unittest

class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass method execution")
    # def setUp(self):
    #     print("setup method execution")
    # def tearDown(self):
    #     print("teardown method execution")
    def test1(self):
        print("test1 method1 execution")
    def test2(self):
        print("test2 method2 execution")
        # print(10/0)
    def test(self):
        print("test method execution")
    @classmethod
    def tearDownClaas(cls):
         print("teardownclass method execution")
unittest.main() 