"""
assume x * y = z
if z > 10 000 (5 digits) then x*y combined need to occupy 4 digits
99 * 99 < 10 000, 9 * 999 < 1000
z cannot be 5 digits

if z is 3 digit then x*y need to occupy 6 digits
100* 100, 10*1 000, 1*10 000 >> 999

z is 4 digit number
"""
import math

products = []
for z in range(1000, 10000):
    limit = math.floor(math.sqrt(z))
    for i in range(1, limit + 1):
        if z % i == 0:
            k = str(z) + str(i) + str(z // i)
            if "".join(sorted(k)) == "123456789":
                products.append(z)
sum_prod = 0
for i in set(products):
    sum_prod+=i
print(sum_prod)