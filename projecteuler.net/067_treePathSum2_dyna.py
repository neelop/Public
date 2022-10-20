f = open("p067_triangle.txt", "r")
tree = []
for x in f:
    y = x[:-1].split(" ")
    z = []
    for item in y:
        while item[0] == "0":
            item = item[1:]
        z.append(int(item))
    tree.append(z)
for i in tree:
    print(i)
index_tree = list(range(len(tree) - 1))[::-1]

for i in index_tree:
    for j in range(i + 1):
        if tree[i + 1][j] > tree[i + 1][j + 1]:
            tree[i][j] += tree[i + 1][j]
        else:
            tree[i][j] += tree[i + 1][j + 1]
print(tree[0][0])
