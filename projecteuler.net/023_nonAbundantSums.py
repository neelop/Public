from toolsy_sroolsy import proper_division_v3
from time import time
start = time()
limit = 28123
abundant_numbers = []

for i in range(1, limit):
    if proper_division_v3(i) > i:
        abundant_numbers.append(i)

x = len(abundant_numbers)
a = 0
possible_number = []
for number in abundant_numbers:
    for i in range(a, x):
        z = number + abundant_numbers[i]
        if z < 28123:
            possible_number.append(z)
        else:
            break
    a += 1
possible_number = list(set(possible_number))
minus_sum = 0
for item in possible_number:
    minus_sum += item
result = 0
for item in range(limit):
    result += item
stop = time()
print(result - minus_sum, stop - start)

