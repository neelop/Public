from toolsy_sroolsy import factorization

# TODO slow

i = 2 * 3 * 5 * 7
marker = True

while marker:
    i += 4
    numbers = []
    if len(set(factorization(i))) == 4:
        numbers = [i]
        counter = 1
        for j in range(1, 4):
            if len(set(factorization(i - j))) == 4:
                numbers.append(i - j)
            else:
                break
        if len(numbers) == 4:
            print(sorted(numbers))
            marker = False

        for j in range(1, 4):
            if len(set(factorization(i + j))) == 4:
                numbers.append(i + j)
                if len(numbers) == 4:
                    print(sorted(numbers))
                    marker = False
            else:
                break
