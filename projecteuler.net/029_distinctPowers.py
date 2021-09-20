ans = []
for a in range(2,101):
    for b in range(2,101):
        ans.append(a**b)
print(len(set(ans)))