# unelegant semi-guess, not an algorithm
a = 9699690  # product of multiplication of all primes in 1-20

b = [12, 14, 15, 16, 18, 20]  # contains 4 6 8 10 (like 4,6 is in 12, 8 is in 16)
# aswell as lower primes like 2*3 is 6, 7 is in 14, 5 in 15

c = True

while c:
    a += 461890  # 11*13*17*19*10 (ned 0 at the end)
    d = 0
    for item in b:
        if a % item == 0:
            d += 1
        if d == len(b):
            c = False

print(a)
for i in range(1, 21):
    print(i, a / i)

# algorithms (based on ov)

# assuming we know prime numbers up to n
n = 20
primes = [2, 3, 5, 7, 11, 13, 17, 19]
# sieve can be used for a larger number

from toolsy_sroolsy import factorization

for item in range(2, n):
    if item in primes:
        continue
    k = factorization(item)
    for bitem in k:
        x = k.count(bitem)
        y = primes.count(bitem)
        while y < x:
            primes.append(bitem)
            y = primes.count(bitem)
print(primes)
score = 1
for item in primes:
    score = score * item
print(score)
