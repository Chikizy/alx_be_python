import unittest
from simple_calculator import SimpleCalculator


class Testsimplecalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)
    def test_division(self):
        self.assertEqual(self.calc.divide(60, 10), 6)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 1), 3)
    