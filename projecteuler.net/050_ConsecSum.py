from toolsy_sroolsy import EraSieveOpt, isPrime


def main():
    primes = EraSieveOpt(10 ** 6)
    prime_sums = []
    for i in range(len(primes)):
        a_sum = 0
        counter = 0
        for j in range(i, len(primes)):
            a_sum += primes[j]
            if a_sum in primes:
                counter += 1
            else:
                prime_sums.append((a_sum, counter))
    for item in prime_sums:
        print(item)


if __name__ == '__main__':
    main()
