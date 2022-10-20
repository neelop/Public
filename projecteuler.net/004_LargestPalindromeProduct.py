# unelegant solution

a = 999
b = 999

e = []
while a != 99:
    d = str(a * b)
    if d == d[::-1]:
        e.append((int(d), a, b))
    b = b - 1
    if b == 99:
        a = a - 1
        b = a
print(max(e))
'''        
e.sort()
for item in e:
    print(item)
'''
# not every solution but top 1 (ov)
a = 999
score = 0
while a > 99:
    b = 999
    while b >= a:
        d = a * b
        if d < score:
            break
        if str(d) == str(d)[::-1]:
            score = d
        b = b - 1
    a = a - 1
print(score)

# better (ov)

score = 0
a = 999
while a > 99:
    if a % 11 == 0:
        b = 999
        db = 1
    else:
        b = 990
        db = 11
    while b >= a:
        d = a * b
        if d < score:
            break
        if str(d) == str(d)[::-1]:
            score = d
        b = b - db
    a = a - 1
print(score)
