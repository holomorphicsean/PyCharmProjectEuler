"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import time
import math
import euler_prime_functions as pf

t0 = time.time()
n = 20

# form a list of primes up to n
prime_vec = pf.primes_upto(n)

# do a bit of math...
prime_vec = [i**int(math.log(n, i)) for i in prime_vec]

# Now we multiply each member in the list. Easy!

ans = 1
for i in prime_vec:
    ans *= i

print(ans)

t1 = time.time()
print("Execution time: " + str(t1 - t0) + " seconds.")