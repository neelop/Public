from toolsy_sroolsy import EraSieveOpt, isPrime
from time import time

start = time()

primes = EraSieveOpt(1000000)

circ_primes = []
a = 0

for a_prime in primes:
    str_prime = str(a_prime)
    circles = [int(str_prime[i : ] + str_prime[ : i]) for i in range(len(str_prime))]
    if all([isPrime(circles[i]) for i in range(len(circles))]):
        a+=1

stop = time()

print(a, stop - start)
