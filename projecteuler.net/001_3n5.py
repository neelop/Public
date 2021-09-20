import time

def a3b5(a, b, c):
    # a > b, not necessery, but imo works better
    # a, b required numbers
    # a = 3
    # b = 5
    # limit
    # c = 1000
    score = 0
    for i in range(0, c, a):
        score += i

    k = 0

    for j in range(0, c, b):
        if k != a:
            score += j
            k += 1
        else:
            k = 1
    return(score)


def multiples(number):
    thesum = 0
    i = 0
    while i < (number - 1):
        i += 1
        if i % 3 == 0 or i % 5 == 0:
            thesum += i
    return thesum



a = time.time()
print(a3b5(3, 5, 100000*10000))
b = time.time()
print(b-a)
a = time.time()
print(multiples(100000*10000))
b = time.time()
print(b-a)