
def even(a=0):
    i = 0
    if a % 2 == 1:
        a += 1
    while True:
        yield i + a
        i += 2


def repeat(a=0, k=None):
    if k == None:
        while True:
            yield a
    else:
        for i in range(k):
            yield a

def accumulate(lista):
    #dziala tylko na inty i str, bo nie wiem jak zrobic zeby dziala na wszysko bez przepisywania z dokumentacji
    a = 0
    b=""
    for item in lista:
        if type(item) is int:
            a = a+ item
            yield a
        elif type(item) is str:
            b = b+ item
            yield b

# def accumulate2(lista):
#     it = iter(lista)
#     total = None
#     for item in it:
#         yield item
#         total += item

def xrange(start, stop = None):
    if stop == None:
        stop = start
        start = 0
    i = start
    while i < stop:
        yield i
        i += 1


def main():
    # zad1 - break point jest zeby zobaczyc co sie dzieje "na starcie" bo sie szybko przewija
    for i in even(9):
        print(i)
        if i > 30:
            break
    # zad 2
    for i in repeat(10, 3):
        print(i)
    #zad 3
    for i in accumulate([1,2,3,4,5,6,7,8,9,10]):
        print(i)
    #zad 4
    for i in accumulate(["ziombro"," przestan ","przesladowac"]):
        print(i)
    #zad5
    for  i in xrange(10):
        print(i)


if __name__ == "__main__":
    main()
