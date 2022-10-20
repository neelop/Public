from time import time

# unelegant
# 20 moves to the left, 20 moves down, after using all left/down moves, fill the rest with down/left
# binomial coefficient of 40 over 20

aprod = 1
for i in range(21, 41):
    aprod = aprod * i
bprod = 1
for j in range(1, 21):
    bprod = bprod * j

print(aprod, bprod, aprod / bprod)


# recursive, "prostocie i elegancji metody towarzyszy skrajna nieefektywnosc",
# probably not enough time in the universe
def countroutes1(m, n):
    if n == 0 or m == 0:
        return 1
    return countroutes1(m, n - 1) + countroutes1(m - 1, n)


# recursive memois, works for 200x200, for 2k x 2k too much recursion
M, N = 20, 20
matrix = [[0 for x in range(M + 1)] for y in range(N + 1)]


def countroutes2(m, n):
    if n == 0 or m == 0:
        return 1
    if matrix[m][n] != 0:
        return matrix[m][n]
    matrix[m][n] = countroutes2(m, n - 1) + countroutes2(m - 1, n)
    return matrix[m][n]


start = time()
a = countroutes2(M, N)
stop = time()
print(a, stop - start)


# bottom up
def countroutes3(n, m):
    matrix = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for i in range(m+1):
        matrix[0][i] = 1
    for i in range(n+1):
        matrix[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            matrix[j][i] = matrix[j - 1][i] + matrix[j][i - 1]
    for i in matrix:#dont print large nxm
      print(i)
    return (matrix[n][m])


start = time()
b = countroutes3(M, N)
stop = time()
print(b, stop - start)
