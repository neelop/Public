def triangle_n(n):
    return 1 / 2 * n * (n + 1)


def main():
    f = open("p042_words.txt", "r")
    for x in f:
        b = x.split('","')
    b[0] = b[0][1:]
    b[-1] = b[-1][:-1]

    maks = 0
    for word in b:
        suma = 0
        for letter in word:
            suma += ord(letter) - 64
        if suma > maks:
            maks = suma
    triangle_numbers = []
    x, n = 1, 1
    while x <= maks:
        x = triangle_n(n)
        triangle_numbers.append(x)
        n += 1
    counter = 0
    for word in b:
        suma = 0
        for letter in word:
            suma += ord(letter) - 64
        if suma * 1.0 in triangle_numbers:
            counter += 1
    print(counter)

def main2():
    f = open("p042_words.txt", "r")
    b = f.read().split('","')
    b[0] = b[0][1:]
    b[-1] = b[-1][:-1]

    counter = 0
    triangle_numbers = [1]
    x, n = 1, 2
    for word in b:
        suma = 0
        for letter in word:
            suma += ord(letter) - 64
        while suma > triangle_numbers[-1]:
            x = triangle_n(n)
            triangle_numbers.append(x)
            n += 1
        if suma * 1.0 in triangle_numbers:
            counter += 1
    print(counter)

if __name__ == '__main__':
    main2()
