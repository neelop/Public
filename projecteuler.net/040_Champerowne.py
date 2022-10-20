def main():
    champ = "0"
    i = 1
    while len(champ) <= 10 ** 6:
        champ += str(i)
        i += 1
    result = 1
    print(champ[1], champ[10], champ[100])
    for x in range(1,7):
        result = result * int(champ[10 ** x])
    print(result)




if __name__ == '__main__':
    main()
