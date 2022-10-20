collection = [(0, [0])]

for b in range(1, 1000):
    a = 1
    cycle = []
    answer = []
    while True:
        if a == 0:
            break
        if b > a:
            a = a * 10
            if a < b:
                answer.append(0)
            if a in cycle:
                c = int(a / b)
                answer.append(c)
                break
        else:
            cycle.append(a)
            c = int(a / b)
            answer.append(c)
            a = a - c * b
    collection.append((b, answer))
index = 0
maksik = 0
for i, j in collection:
    if len(j) > maksik:
        maksik = len(j)
        index = i
print(index)


######
import itertools


def compute():
    ans = max(range(1, 1000), key=reciprocal_cycle_len)
    return str(ans)


def reciprocal_cycle_len(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x * 10 % n

reciprocal_cycle_len(7)