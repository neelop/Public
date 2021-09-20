import time
from random import randrange

mylist =[]
for i in range(0, 500000):
    mylist.append(randrange(0, 10000))

def runtime (fun):
    def inner(*arg):
        start = time.time()
        x = fun(*arg)
        stop = time.time()
        print(" Runtime of",fun.__name__ , "() was ",stop - start, " seconds .")
        return x
    return inner
@runtime
def sort1(a):
    a.sort()
    return a
@runtime
def sort2(b) :
    for i in range(1, len(b)):
        elementToInsert = b[i]
        previouseElement = i - 1
        while previouseElement >= 0 and b[previouseElement] > elementToInsert:
            b[previouseElement + 1] = b[previouseElement]
            previouseElement -= 1
        b[previouseElement + 1] = elementToInsert
    return b

sort1(mylist)
sort2(mylist)
