def gen_hex(n):
    return n * (2 * n - 1)


def is_penta(n):
    if ((24 * n + 1) ** 0.5 + 1) % 6 == 0:
        return True
    else:
        return False

def is_tria(n):
    """
    irreleant, every triangle number is hexagonal number
    :param n:
    :return:
    """
    if ((8 * n + 1) ** 0.5 - 1) % 2 == 0:
        return True
    else:
        return False


def main():
    i = 143
    marker = True
    while marker:
        i += 1
        a = gen_hex(i)
        if is_penta(a):
            marker = False
            print(a)
if __name__ == '__main__':
    main()
