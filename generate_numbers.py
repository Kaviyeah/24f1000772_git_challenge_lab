def natural_numbers(n):
    """
    Returns the list of natural numbers from 1 to n
    """
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers


def nth_fibonacci(n):
    """
    Returns the n-th Fibonacci number
    (1st Fibonacci = 0, 2nd Fibonacci = 1)
    """
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    """
    Returns True if n is a prime number, otherwise False
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
