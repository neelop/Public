# generator liczb losowych "marsenne twister"

class MersenneTwister:

    def __init__(self, seed=1111):
        self.seed = seed
        self.mersenne = 2 ** 31 - 1
        self.pomoc = 16807

    def calkowita(self, zakres=None, count=1):
        results = []
        for i in range(count):
            self.seed = (self.pomoc * self.seed) % self.mersenne
            if zakres is not None:
                results.append(int((zakres[1] - zakres[0] + 1) * (self.seed / self.mersenne) + zakres[0]))
            else:
                result = self.seed / self.mersenne
                if result < 0.50:
                    results.append(0)
                else:
                    results.append(1)
        if count == 1:
            return results.pop()
        else:
            return results



def sort_srort(lista):
    kopia = lista.copy()
    najwieksza = max(kopia)
    najmniejsza = min(kopia)
    if najmniejsza < 0:
        najwieksza -= najmniejsza
    else:
        najmniejsza = 0
    #print(najwieksza, najmniejsza)
    result = []
    for i in range(najwieksza + 1):
        result.append(0)
    for item in kopia:
        result[item - najmniejsza] += 1
    #print(result)
    wynik = []
    for bitem in range(najwieksza + 1):
        while result[bitem] != 0:
            wynik.append(bitem + najmniejsza)
            result[bitem] -= 1
    return wynik


a = MersenneTwister(1234)
b = a.calkowita((-99, 99), 10)
#print(b)
c = b.copy()
d = b.copy()
c = sort_srort(c)  # moj sort
d.sort()  # nie moj sort
print(c, "\n", d)
