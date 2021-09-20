class count:
    def __iter__(self):
        return self

    def __init__(self, start=0):
        self.start = start

    def __next__(self):
        x = self.start
        self.start += 1
        return x


class tetranacci:
    def __init__(self, steps=25):
        self.steps = steps
        self.tetr0 = 0
        self.tetr1 = 0
        self.tetr2 = 0
        self.tetr3 = 1
        self.mark = 0

    def __iter__(self):
        return self

    def __next__(self):
        x = self.tetr0
        self.mark += 1
        if self.mark > self.steps:
            raise StopIteration
        self.tetr0, self.tetr1, self.tetr2, self.tetr3 = self.tetr1, self.tetr2, self.tetr3, self.tetr0 + self.tetr1 + self.tetr2 + self.tetr3
        return x


class repeat:
    def __init__(self, elem=0, times=None):
        self.elem = elem
        self.times = times
        self.mark = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.times == None:
            return self.elem
        else:
            if self.mark >= self.times:
                raise StopIteration
            self.mark += 1
            return self.elem


class odd_first:
    def __init__(self, lista):
        self.ace = []
        self.bdf = []
        for i in lista:
            if lista.index(i) % 2 == 0:
                self.ace.append(i)
            else:
                self.bdf.append(i)
        self.lista = self.ace + self.bdf
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.lista):
            raise StopIteration
        else:
            self.i += 1
            return self.lista[self.i - 1]


class chain:
    def __init__(self, *args):
        self.lista = args
        self.z = []
        for item in self.lista:
            for atom in item:
                self.z.append(atom)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.z):
            raise StopIteration
        else:
            self.i += 1
            return self.z[self.i - 1]


def main():
    zad1 = count(int(input("zad 1, input: ")))
    for i in range(0, 10):
        print(next(zad1))
    zad2 = tetranacci(int(input("zad 2, input ")))
    print(list(zad2))
    for i in zad2:
        print(i)
    zad3 = repeat(7, 3)
    print(list(zad3))
    for i in zad3:
        print(i)
    zad4 = odd_first("ziobrotykurwojebana")
    print(list(zad4))
    zad5 = chain("123", "3214", "21341")
    print(list(zad5))


if __name__ == '__main__':
    main()
