from time import time

# brute force

start = time()
size = 1001  # uneven/odd


def check_direction(matrix, x, y, direction):
    matr = matrix.copy()
    if matr[y][x + 1] == 0 and matr[y + 1][x] == 0 and matr[y - 1][x] == 0:
        return "s"
    if matr[y][x + 1] == 0 and matr[y + 1][x] == 0 and matr[y][x - 1] == 0:
        return "w"
    if matr[y][x - 1] == 0 and matr[y + 1][x] == 0 and matr[y - 1][x] == 0:
        return "n"
    if matr[y][x + 1] == 0 and matr[y - 1][x] == 0 and matr[y][x - 1] == 0:
        return "e"
    return direction


size = size + 2
matrix = [[0 for x in range(size)] for y in range(size)]
h = int(size / 2)
matrix[h][h] = 1
x = h + 1
y = h
z = 2

direction = "e"
while True:
    if matrix[1][size - 2] != 0:
        break
    matrix[y][x] = z
    z += 1
    direction = check_direction(matrix, x, y, direction)
    if direction == "e":
        x += 1
    elif direction == "s":
        y += 1
    elif direction == "w":
        x = x - 1
    elif direction == "n":
        y = y - 1

suma = 0
for i in range(size):
    suma += matrix[i][i] + matrix[i][size - 1 - i]
stop = time()
print(suma - 1, stop - start)  # middle was added twice

# smarter
"""
odd-size matrix will always have in the last corner n^2.
matrix size 3 will have 9, size 5 25.
from that we simply count back corners
"""
start = time()
suma = 1
for n in range(3, 1002, 2):
    k = n * n
    suma += k
    for i in range(1, 4):
        k = k - n + 1
        suma += k
stop = time()
print(suma, stop - start)
