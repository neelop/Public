from math import floor

def multiply(liczba, tuplet=(1, 2, 3)):
    zwrot = ""
    for number in tuplet:
        zwrot += str(number * liczba)
    return zwrot


# print("".join(sorted(multiply(192))))
# print(multiply(9 , [1,2,3,4,5]))
# print( multiply(192, range(1,4)))

def main():
    tuplet = 2
    results = []
    while tuplet < 10:
        for liczba in range(1, 10 ** 4):
            asd = multiply(liczba,range(1,tuplet))
            if len(asd) == 9:
                if "".join(sorted(asd)) == "123456789":
                    results.append([int(asd), liczba, list(range(1,tuplet)) ])
        tuplet += 1
    results.sort(reverse=True)
    for item in results:
        print(item)

if __name__ == "__main__":
    main()
