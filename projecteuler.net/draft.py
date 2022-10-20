def POTEZNY(sznurek):
    napis = sznurek.lower()
    napis = "".join(napis.split(" ")).upper()
    zwrot = ""
    for i in napis:
        zwrot += i+" "
    print(zwrot)

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(parrot(**d))

# matrix = [[x for x in range(5)] for y in range(10)]
# print(matrix[0][1])

POTEZNY("")

"""from random import randrange
from time import time
start = time()
do_sredniej = []
for i in range(50000000):
    oczka = 0
    kostki = []
    for i in range(4):
        x = randrange(1,7)
        kostki.append(x)
    kostki.sort()
    kostki = kostki[1:]
    oczka = sum(kostki)
    do_sredniej.append(oczka)

avg = sum(do_sredniej)/len(do_sredniej)
stop = time()
print(avg, stop-start)"""

from random import randrange
oczka = 0
kostki = []
for i in range(4):
    x = randrange(1,7)
    kostki.append(x)
kostki.sort()
kostki = kostki[1:]
oczka = sum(kostki)
print(oczka)






"""a jak cos tu dopisze
"""








