from toolsy_sroolsy import factorization, EraSieveOpt
import time

time1 = time.time()
a = 8
suma = 28  # 7th triangular number

while True:
    count = 1
    suma += a
    a += 1
    x = factorization(suma)
    y = list(set(x))
    for item in y:
        e = x.count(item) + 1
        count = count * e
    if count > 500:
        print(suma)
        break
time2 = time.time()
print(time2-time1)

# from OV
x = time.time()
P = 1000
primes = EraSieveOpt(P)
n = 3
Dn = 2
cnt = 0
while cnt <= 500:
    n = n + 1
    n1 = n
    if n1 % 2 == 0:
        n1 = n1 / 2
    Dn1 = 1
    for i in range(P):
        if primes[i] * primes[i] > n1:
            Dn1 = Dn1 * 2
            break
        exponent = 1
        while n1 % primes[i] == 0:
            exponent += 1
            n1 = n1 / primes[i]
        if exponent > 1:
            Dn1 = Dn1 * exponent
        if n1 == 1:
            break
    cnt = Dn * Dn1
    Dn = Dn1
y = time.time()
print((n * (n - 1)) / 2)
print(y - x)
