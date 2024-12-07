import unittest
from funcoes import Calculator

class TestCalculator(unittest.TestCase):

    def test_positive_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_negative_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(-2, -3), -5)

    def test_invalid_add(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.add(2, "3")
    
    def test_positive_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(2, 3), -1)

    def test_negative_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(-2, -3), 1)

    def test_invalid_subtract(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.subtract(2, "3")

    def test_positive_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(2, 3), 6)

    def test_negative_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(-2, -3), 6)

    def test_invalid_multiply(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.multiply(2, "3")

    def test_positive_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(6, 3), 2)
    
    def test_negative_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(-6, -3), 2)

    def test_invalid_divide(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.divide(6, "3")
    
    def test_zero_divide(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(6, 0)
    
    def test_concat(self):
        calc = Calculator()
        self.assertEqual(calc.concat("hello", "world"), "helloworld")
    
    def test_invalid_concat(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.concat("hello", 3)

if __name__ == '__main__':
    unittest.main()