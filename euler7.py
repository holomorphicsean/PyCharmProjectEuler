"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

# luckily we have just the function in euler_prime_functions!
import time
import euler_prime_functions as pf

t0 = time.time()
print(pf.prime(10001))
t1 = time.time()
print("Execution: " + str(t1 - t0) + " seconds.")