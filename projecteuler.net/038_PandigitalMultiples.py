from time import time


def multiply(liczba, tuplet=(1, 2, 3)):
    zwrot = ""
    for number in tuplet:
        zwrot += str(number * liczba)
    return zwrot


# print("".join(sorted(multiply(192))))
# print(multiply(9 , [1,2,3,4,5]))
# print( multiply(192, range(1,4)))

def main():
    start = time()
    results = []
    for tuplet in range(2, 10):
        for liczba in range(1, 10 ** (9 // tuplet)):
            asd = multiply(liczba, range(1, tuplet + 1))
            if len(asd) == 9:
                if "".join(sorted(asd)) == "123456789":
                    results.append([int(asd), liczba, list(range(1, tuplet + 1))])
    results.sort(reverse=True)
    stop = time()
    for item in results:
        print(item)
    print(stop - start)

if __name__ == "__main__":
    main()
