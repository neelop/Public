def triangle_n(n):
    return 1 / 2 * n * (n + 1)


def main():
    f = open("p042_words.txt", "r")
    for x in f:
        b = x.split('","')
    b[0] = b[0][1:]
    b[-1] = b[-1][:-1]

    max = 0
    for word in b:
        sum = 0
        for letter in word:
            sum += ord(letter) - 64
        if sum > max:
            max = sum
    triangle_numbers = []
    x, n = 1, 1
    while x <= max:
        x = triangle_n(n)
        triangle_numbers.append(x)
        n += 1
    counter = 0
    for word in b:
        sum = 0
        for letter in word:
            sum += ord(letter) - 64
        if sum* 1.0 in triangle_numbers:
            counter +=1
    print(counter)


if __name__ == '__main__':
    main()
