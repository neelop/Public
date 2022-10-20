from time import time


def swap_positions(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    return lista


a = [i for i in range(10)]
i = 1
b = list(range(10))[::-1]
start = time()
marker = True

while marker:
    if i == 1000000:
        break
    # find non-increasing suffix
    for j in b:
        if j == 0:
            # last permutation
            marker = False
        elif a[j] > a[j - 1]:
            # set up a pivot
            pivot = j - 1
            # split
            a_prefix = a[:pivot]
            a_suffix = a[pivot:]
            # find the rightmost succesor to pivot in suffix
            b_prim = list(range(len(a_suffix)))[::-1]
            for k in b_prim:
                if a_suffix[k] > a_suffix[0]:
                    # swap suffix with succesor
                    swap_positions(a_suffix, 0, k)
                    break
            a_pivot = [a_suffix[0]]  # get pivot
            a_suffix_prim = a_suffix[1:]  # get remaining suffix
            # return with reversed suffix and changed pivot
            a = a_prefix + a_pivot + a_suffix_prim[::-1]
            break
    i += 1
stop = time()
string = ""
for i in a:
    string += str(i)
print(string, stop - start)
