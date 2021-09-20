from toolsy_sroolsy import EraSieveOpt, isPrime
from itertools import count
from time import time
start = time()
# f(n) = n^2 + an + b, f(0) needs to be a prime, f(0) = b, so b needs to be positive and prime
b_candidates = EraSieveOpt(1000)
a_candidates = list(range(-999, 1000))
answr = []

for a in a_candidates:
    for b in b_candidates:
        for n in count():
            k = n * n + a * n + b
            if not isPrime(k):
                answr.append((n, a, b))
                break

stop = time()
k = answr.index((max(answr)))
print(answr[k])
print(answr[k][1]*answr[k][2])
print(stop-start)
