import math


def factorization(n):
    k = 2
    dividers = []
    while n % k == 0:
        n = n / k
        dividers.append(k)
    k += 1
    while n != 1:
        if n % k == 0:
            while n % k == 0:
                n = n / k
                dividers.append(k)
        k += 2
    return dividers


def isPrime(n):
    if n < 0:
        return False
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


def EraSieve(number):
    limit = math.floor(math.sqrt(number))
    sieve = [False for i in range(number + 1)]
    for i in range(4, number + 1, 2):
        sieve[i] = True
    for n in range(3, limit + 1, 2):
        if not sieve[n]:
            for m in range(n * n, number + 1, 2 * n):
                sieve[m] = True
    sieve[0] = True
    sieve[1] = True
    result = []
    for item in range(0, number + 1):
        if not sieve[item]:
            result.append(item)
    return result


def EraSieveOpt(number):
    sievebound = int((number + 1) / 2)
    sieve = [False for i in range(sievebound)]
    limit = int(math.floor(math.sqrt(number)) / 2) + 1
    for i in range(1, limit):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sievebound, 2 * i + 1):
                sieve[j] = True
    result = [2]
    for i in range(1, sievebound):
        if not sieve[i]:
            result.append(2 * i + 1)
    return result


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


def main():
    """
    test unit kek
    :return:
    """
    EraSieve(25)


if __name__ == "__main__":
    main()
