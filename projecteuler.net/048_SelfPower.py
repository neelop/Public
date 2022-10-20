def main():
    limit = 10 ** 10
    a = []
    for i in range(1, 1000):
        a.append(pow(i, i, limit))
    print(sum(a) % limit)


def main2():
    limit = 10 ** 10
    print(sum([pow(i, i, limit) for i in range(1, 1000)]) % limit)


if __name__ == '__main__':
    main()
    main2()
