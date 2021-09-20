"""
x = 9! = 362 880  (6digits)
6x 2 177 280 (7digits)
7x 2 540 160 (7digits)
8x 2 903 040 (7 digits, cannot reach 8 digits with 8*9!)

so we need to check numebr up to 10**8
"""
from math import factorial
from time import time
start = time()

total = 0

for i in range(3, 2540160):
    number = str(i)
    sum_a = 0
    for num in number:
        sum_a += factorial(int(num))
    if sum_a == i:
        total += i

stop = time()
print(total,stop - start)
