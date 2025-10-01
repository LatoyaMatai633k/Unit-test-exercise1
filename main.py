def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    result = 1
    for i in range(1, n + 1):  # multiply numbers from 1 up to n
        result *= i
    return result


def fibonacci(n):
    """Returns the nth number in the Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fizzbuzz(n):
    """
    Returns a list for the FizzBuzz game up to n.
    - Multiples of 3 are "Fizz"
    - Multiples of 5 are "Buzz"
    - Multiples of both 3 and 5 are "FizzBuzz"
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result
