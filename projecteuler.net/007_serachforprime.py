from toolsy_sroolsy import factorization
import math

primes = []
k = 2
while len(primes) < 10001:
    if len(factorization(k)) == 1:
        primes.append(k)
    k += 1

#print(primes.pop())

"""
All primes greater than 3 can be written in the form  6k+/-1.
Any number n can have only one primefactor greater than sqrt n.
The consequence for primality testing of a number n is: 
if we cannot find a number f less than or equal sqrt n 
that divides n then n is prime:
 the only primefactor of n is n itself
"""


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    limit = math.floor(math.sqrt(n))
    f = 5
    while f <= limit:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

primavera = []

k = 1
while len(primavera) < 10001:
    if isPrime(k):
        primavera.append(k)
    k+=2

print(primavera.pop())

