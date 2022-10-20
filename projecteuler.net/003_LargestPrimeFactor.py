n = 600851475143


def LargestPrimeFinder(n):
    k = 2
    dzielniki = []
    while n % k == 0:
        n = n / k
        dzielniki.append(k)
    k += 1
    while n != 1:
        if n % k == 0:
            while n % k == 0:
                n = n / k
                dzielniki.append(k)
        k += 2
    return dzielniki


print(max(LargestPrimeFinder(n)))
