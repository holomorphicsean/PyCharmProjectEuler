"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

import time
import math


# checks that a number is a palindrome
def is_palindrome(n):

    # turn number into list
    digs = [int(i) for i in str(n)]
    return digs == digs[::-1]


# function to count the number of digits in a number
def num_digs(n):

    return math.floor(math.log(n,10)+1)


# function to break a product into 2 k-digit numbers
def product_breaker(k, n):

    # run through all numbers which have k digits
    for i in xrange(10**(k-1), 10**k):

        # if i divides n AND has the same number of digits k, we have our answer
        if n % i == 0 and num_digs(n / i) == k:
            return [n/i, i]

    # if it is not the case, then our program returns False
    return False


if __name__ == '__main__':

    t0 = time.time()

    k = 3  # number of digits we want to split our number into

    # We are going to check our products from the top going down, skipping non-palindromic numbers
    n = ((10**k)-1)**2
    while n > 0:

        if is_palindrome(n):
            prod = product_breaker(k,n)
            if prod:
                break
        n -= 1

    print(prod)

    t1 = time.time()
    print("Execution time: " + str(t1 - t0) + " seconds.")

