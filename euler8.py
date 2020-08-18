"""The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.

(num in txt file)

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?"""

import time

t0 = time.time()

# import number from file
with open('euler8_num.txt') as f:
    num = f.read()

f.close()
# break number into a big list
num = [int(i) for i in num if i != '\n']

# initialize our ans
ans = 0

# now search for the greatest product
for i in range(len(num)-3):
    prod = num[i]*num[i+1]*num[i+2]*num[i+3]
    if prod > ans:
        ans = prod

print(ans)

t1 = time.time()
print("Execution: " + str(t1 - t0) + " seconds.")