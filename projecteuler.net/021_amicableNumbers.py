from time import time

range_number = 10000

def proper_division(number):
    counter = 0
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            counter += i
    return counter


def main():
    x = time()
    counter = 0
    for a in range(2, range_number):
        b = proper_division(a)
        if b > a:
            if proper_division(b) == a:
                counter += a + b
    y = time()
    print(counter, y - x)


if __name__ == "__main__":
    main()

# improved (ov)
import math


def proper_division_v2(n):
    if n == 1:
        return 0
    else:
        r = math.floor(math.sqrt(n))
        if r * r == n:
            counter = 1 + r
            r = r - 1
        else:
            counter = 1
    if n % 2 == 1:
        f = 3
        step = 2
    else:
        f = 2
        step = 1
    while f <= r:
        if n % f == 0:
            counter += f + int(n / f)
        f += step
    return counter


def proper_division_v3(a):
    n = a
    counter = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = int(n / p)
            while n % p == 0:
                j = j * p
                n = int(n / p)
            counter = counter * (j - 1)
            counter = int(counter / (p - 1))
        if p == 2:
            p = 3
        else:
            p += 2
    if n > 1:
        counter = counter * (n + 1)
    return counter - a


def mainv2():
    x = time()
    counter = 0
    for a in range(2, range_number):
        b = proper_division_v2(a)
        if b > a:
            if proper_division(b) == a:
                counter += a + b
    y = time()
    print(counter, y - x)
    x = time()
    counter = 0
    for a in range(2, range_number):
        b = proper_division_v3(a)
        if b > a:
            if proper_division(b) == a:
                counter += a + b
    y = time()
    print(counter, y - x)

mainv2()