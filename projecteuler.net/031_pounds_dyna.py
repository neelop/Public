from time import time

"""
# correct answer but poo algorithm, waste of time to run, ~360s



start = time()

answ = 0

for p50 in range(5):
    for p20 in range(11):
        for p10 in range(21):
            for p5 in range(41):
                for p2 in range(101):
                    for p1 in range(201):
                        k = p1 + 2 * p2 + 5 * p5 + 10 * p10 + 20 * p20 + 50 * p50
                        if k == 100:
                            answ += 1
                        elif k == 200:
                            answ += 1
stop = time()
print(answ +2, stop - start) #+2 coz 100p+100p and 0+200p
"""

# recursive, works fine on 200, not so fine on 2000

coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]  # 0 so 1 index is 1, 2 index is 2, 5index is 3 ...
amount = 200


def ways1(target, avc):
    if avc <= 1:
        return 1
    res = 0
    while target >= 0:
        res = res + ways1(target, avc - 1)
        target = target - coins[avc]
    return res


start = time()
a = ways1(amount, 8)
stop = time()
print(a, stop - start)

# recursive with memoization, can do bigger numbers (top down)

# coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]  # 0 so 1 index is 1, 2 index is 2, 5index is 3 ...
# amount = 2000
memo = [[0 for x in range(9)] for y in range(amount + 1)]


def ways2(target, avc):
    if avc <= 1:
        return 1
    t = target
    if memo[t][avc] > 0:
        return memo[t][avc]
    res = 0
    while target >= 0:
        res = res + ways2(target, avc - 1)
        target = target - coins[avc]
    memo[t][avc] = res
    return res


start = time()
a = ways2(amount, 8)
stop = time()
print(a, stop - start)

# bottom up, lightning fast

coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]  # 0 so 1 index is 1, 2 index is 2, 5index is 3 ...
amount = 200
ways = [0 for x in range(0, amount + 1)]
ways[0] = 1
for i in range(1,9):
    for j in range(coins[i],amount+1):
        ways[j] = ways[j] + ways[j-coins[i]]
print(ways[amount])
for i in ways:
    print(i)