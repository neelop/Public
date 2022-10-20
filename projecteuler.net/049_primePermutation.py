from toolsy_sroolsy import EraSieveOpt
from itertools import permutations

primes = EraSieveOpt(10 ** 4)
for i in primes:
    if i < 999:
        primes = primes[1:]
# comment

