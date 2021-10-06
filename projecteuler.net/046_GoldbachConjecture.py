from toolsy_sroolsy import isPrime

primes = [2, 3, 5, 7]
composites = []
i = 7
marker = True

while marker:
    i += 2
    if not isPrime(i):
        counter = 0
        for number in primes:
            x = ((i - number) / 2) ** 0.5
            if x == int(x):
                break
            else:
                counter += 1
        if counter == len(primes):
            marker = False
            print(i)
    else:
        primes.append(i)
