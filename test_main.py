import unittest
from main import factorial, fibonacci, fizzbuzz  

class TestMyFunctions(unittest.TestCase):
    """Tests for factorial, fibonacci and fizzbuzz."""

    def test_factorial(self)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_fibonacci(self)
        self.assertEqual(fibonacci(7), 13
        self.assertEqual(fibonacci(0), 0)

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(5), [1, 2, "Fizz", 4, "Buzz"])
        self.assertEqual(fizzbuzz(3), [1, 2, "Fizz"])

if __name__ == "__main__":
    unittest.main()
