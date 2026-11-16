import unittest
from factorial import calculate_factorial

class TestFactorial(unittest.TestCase):
    def test_zero_and_one(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)

    def test_positive_numbers(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(7), 5040)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-3)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_factorial(3.5)
        with self.assertRaises(TypeError):
            calculate_factorial("5")

if __name__ == "__main__":
    unittest.main()
