#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer n using recursion.
    The factorial of a number n is the product of all positive integers less than or equal to n.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial value of n (n!). Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
