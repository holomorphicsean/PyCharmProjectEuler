"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

import time


# this function returns the smallest prime factor of n
def smallest_factor(n):

    # base cases
    if n % 2 == 0:
        return 2

    if n % 3 == 0:
        return 3

    # now we run through every number until we get our answer
    k = 5
    while True:
        if n % k == 0:
            return k
        k += 2


if __name__ == '__main__':

    t0 = time.time()

    # our number to check
    n = 600851475143

    # we are going to pull factors out of n until it is equal to 1
    while n != 1:
        sf = smallest_factor(n)
        n = n / sf

    print(sf)

    t1 = time.time()
    print("Execution time: " + str(t1 - t0) + " seconds.")