from toolsy_sroolsy import isPrime
from time import time


def check_truncatability(number):
    number_str = str(number)
    evens = ["4", "6", "8", "0"]
    for i in evens:
        if i in number_str:
            return False
    if not isPrime(int(number_str[0])) or not isPrime(int(number_str[-1])):
        return False
    number_reverse = number_str
    while len(number_str) != 0:
        if not isPrime(int(number_str)) or not isPrime(int(number_reverse)):
            return False
        number_str = number_str[:-1]
        number_reverse = number_reverse[1:]
    return True


start = time()
ssum = 0
counter = 0
i = 11  # probably could use sieve but did not know upper limit, so would be semi guess
while counter < 11:
    if isPrime(i):
        if check_truncatability(i):
            ssum += i
            counter += 1
            # print(i)
    i += 2
stop = time()
print(ssum, stop - start)
