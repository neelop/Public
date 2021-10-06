def is_penta(n):
    if ((24 * n + 1) ** 0.5 + 1) % 6 == 0:
        return True
    else:
        return False


def main():
    """
    Pn+1 - Pn = (n+1)(3(n+1)-1)/2 - n(3n-1)/2 = 3n + 1
    meaning, the further into progression, the numbers are further apart, so
    if we start from the bottom the first number we meet will be the lowest |Pk -Pj|
    """

    marker = True
    i = 2
    pen_nums = [1, 5]
    while marker:
        i += 1
        a = i * (3 * i - 1) / 2
        for number in pen_nums:
            if is_penta(a + number) and is_penta(a - number):
                marker = False
                print(a - number)
        pen_nums.append(a)


if __name__ == '__main__':
    main()
