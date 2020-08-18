"""A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 2**5 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

import time
import math

# We are going to just brute force this and check all combinations
# until we come across our answer

t0 = time.time()

for a in range(1,1000+1):
    for b in range(a,1000+1):
        c = math.sqrt(a**2 + b**2)

        # if c is not an integer forget it
        if c != int(c):
            continue

        # now we check if we hit the special triplet
        if a + b + c == 1000:
            print(int(a*b*c))
            break

t1 = time.time()
print("Execution time: " + str(t1 - t0) + " seconds.")