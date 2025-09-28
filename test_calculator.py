# test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """
    Unit test suite for the Calculator class.
    """

    def setUp(self):
        """
        This method is called before each test function.
        We create a new instance of the Calculator for each test.
        """
        self.calc = Calculator()

    def test_square_root(self):
        """Test the square_root method."""
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertAlmostEqual(self.calc.square_root(2), 1.41421356)
        # Test for expected failure (ValueError) with a negative number
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)

    def test_factorial(self):
        """Test the factorial method."""
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)
        # Test for expected failure with a negative number
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
        # Test for expected failure with a non-integer
        with self.assertRaises(ValueError):
            self.calc.factorial(1.5)

    def test_natural_log(self):
        """Test the natural_log method."""
        self.assertAlmostEqual(self.calc.natural_log(1), 0)
        self.assertAlmostEqual(self.calc.natural_log(2.71828), 1, places=5)
        # Test for expected failure with zero
        with self.assertRaises(ValueError):
            self.calc.natural_log(0)

    def test_power(self):
        """Test the power method."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertAlmostEqual(self.calc.power(9, 0.5), 3)


if __name__ == '__main__':
    unittest.main()