# calculator.py
import math

class Calculator:
    """
    A simple scientific calculator class.
    """

    def square_root(self, x):
        """
        Calculates the square root of a number.
        """
        if x < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(x)

    def factorial(self, x):
        """
        Calculates the factorial of a non-negative integer.
        """
        if not isinstance(x, int) or x < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        return math.factorial(x)

    def natural_log(self, x):
        """
        Calculates the natural logarithm (base e) of a number.
        """
        if x <= 0:
            raise ValueError("Natural logarithm is only defined for positive numbers.")
        return math.log(x)

    def power(self, x, b):
        """
        Calculates x raised to the power of b.
        """
        return math.pow(x, b)