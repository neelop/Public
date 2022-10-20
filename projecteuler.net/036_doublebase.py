

ssum = 0
for i in range(10**6):
    k = str(i)
    if k == k[::-1]:
        s = str(bin(i))[2:]
        if s == s[::-1]:
            ssum += i
print(ssum)

#TODO ov generator

