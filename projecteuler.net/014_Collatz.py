import time

y = time.time()
known_chain = {}
for a in range(2, 1000000):
    chain_count = 1
    n = a
    while n != 1:
        if n in known_chain:
            chain_count += known_chain[n] - 1
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        chain_count += 1
    known_chain[a] = chain_count
max_key = max(known_chain, key=lambda k: known_chain[k])
z = time.time()
print(max_key, z - y)
