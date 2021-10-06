from itertools import permutations


def main():
    suma = 0
    x = "0123456789"
    a = list(permutations(x))
    for i in a:
        i = "".join(i)
        if i[0] != "0":
            marker = 0

            if int(i[1] + i[2] + i[3]) % 2 != 0:
                marker += 1
            elif int(i[2] + i[3] + i[4]) % 3 != 0:
                marker += 1
            elif int(i[3] + i[4] + i[5]) % 5 != 0:
                marker += 1
            elif int(i[4] + i[5] + i[6]) % 7 != 0:
                marker += 1
            elif int(i[5] + i[6] + i[7]) % 11 != 0:
                marker += 1
            elif int(i[6] + i[7] + i[8]) % 13 != 0:
                marker += 1
            elif int(i[7]+i[8]+i[9]) % 17 != 0:
                marker += 1

            if marker == 0:
                suma += int(i)
                print(i)
    print(suma)


if __name__ == '__main__':
    main()
