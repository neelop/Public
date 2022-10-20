from toolsy_sroolsy import isPrime
from itertools import permutations

def main():
    z = "123456789"
    marker = True
    while marker:
        a = list(permutations(z))
        a = a[::-1]
        for i in a:
            i = int("".join(i))
            if isPrime(i):
                print(i)
                marker = False
                break
        z = z[:-1]

if __name__ == '__main__':
    main()

