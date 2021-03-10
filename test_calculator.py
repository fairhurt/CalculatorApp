import unittest
from calculator import addition 
from calculator import subtraction 
from calculator import division 
from calculator import multiplication

class TestCalc(unittest.TestCase):
    def test1(self):
        self.assertEqual(addition(2,3) , 5)

    def test2(self):
        self.assertEqual(subtraction(5,3) , 2)

    def test3(self):
       self.assertEqual(multiplication(2,3) , 6)
    def test4(self):
        self.assertEqual(division(9,3) , 3)




  
if __name__ == '__main__':
    unittest.main(verbosity=2)
        
        