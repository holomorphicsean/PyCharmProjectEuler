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


# function that returns a list of primes up to n
def primes_upto(n):

    # base cases
    if n == 2:
        return [2]
    if n == 3 or n == 4:
        return [2,3]

    # main program
    vec = [2,3]
    k = 5
    while k <= n:
        if not is_prime(k):
            k += 2
            continue

        vec.append(k)
        k += 2

    return vec


# rough function for getting nth prime
def prime(n):

    count = 0
    k = 1   # generates numbers until we reach our desired count
    while True:
        if is_prime(k):
            count += 1

        if count == n:
            break
        k += 1

    return k


# same as primes_upto function but using a sieve
def primes_upto_sieve(n):

    # create our list to distill out our primes
    to_sieve = range(2, n+1)

    # our method will be to pop off the first element into a growing list of primes
    # then delete all of its multiples

    primes = []
    while to_sieve:
        primes.append(to_sieve.pop(0))
        to_sieve = [i for i in to_sieve if i % primes[-1] != 0]

    return primes


