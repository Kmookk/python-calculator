import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    #Add
    def test_add_1(self):
        self.assertIsInstance(self.calc.add(1.6,2.5),float)

    def test_add_2(self):
        self.assertGreater(self.calc.add(1,2),2)

    # #Subtract
    def test_subtract_1(self):
        self.assertGreater(self.calc.subtract(4,2),0)

    def test_subtract_2(self):
        self.assertLess(self.calc.subtract(-4,-2),0)

    def test_subtract_3(self):
        self.assertEqual(self.calc.subtract(-2,-2),0)

    def test_subtract_4(self):
        self.assertLess(self.calc.subtract(-2,5),0)

    def test_subtract_5(self):
        self.assertGreater(self.calc.subtract(7,-2),0)

    def test_subtract_6(self):
        self.assertLess(self.calc.subtract(-7,2),0)

    # #Multiplication
    def test_multi_1(self):
        self.assertEqual(self.calc.multiply(2,3),6)

    def test_multi_2(self):
        self.assertEqual(self.calc.multiply(2,0),0)

    def test_multi_3(self):
        self.assertLess(self.calc.multiply(2,-6),0)

    def test_multi_4(self):
        self.assertGreater(self.calc.multiply(-2,-6),0)

    # #divide 
    def test_divide_1(self):
        self.assertEqual(self.calc.divide(10,2),5)
    
    def test_divide_2(self):
        self.assertLess(self.calc.divide(-10,2),0)

    def test_divide_3(self):
        self.assertLess(self.calc.divide(10,-2),0)

    def test_divide_4(self):
        self.assertGreater(self.calc.divide(-10,-2),0)

    def test_divide_5(self):
        self.assertEqual(self.calc.divide(10,10),1)
    
    # #modulo 
    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(10,3),1)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(4,1),0)

    def test_modulo_3(self):
        self.assertEqual(self.calc.modulo(4,4),0)

if __name__ == '__main__':
    unittest.main()
