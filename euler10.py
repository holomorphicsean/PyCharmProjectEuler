"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

import time
import euler_prime_functions as pf

t0 = time.time()
print(sum(pf.primes_upto(2*10**6)))
t1 = time.time()
print("Execution: " + str(t1-t0) + " seconds.")