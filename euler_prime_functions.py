# This file contains various functions related to prime numbers for use by other programs
import math
import sys


def is_prime(n):
    # n needs to be a positive integer
    if n != int(n) or n < 1:
        print("n must be a positive integer. Program aborting.")
        sys.exit()

    # 1 is not prime
    if n == 1:
        return False

    # base case checks
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check all divisors up to sqrt(n), and only check of the form 6*k + 1
    k = 1
    while 6*k - 1 <= math.sqrt(n):
        if n % (6*k - 1) == 0 or n % (6*k + 1) == 0:
            return False
        k += 1

    return True

