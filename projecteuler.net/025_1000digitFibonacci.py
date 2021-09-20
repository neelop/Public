from time import time
start = time()
limit = 10 ** 999
print(len(str(limit)))
a1 = 1
a2 = 2
i = 3
score_list = [a1, a2]
while True:
    a = score_list[0] + score_list[1]
    if a < limit:
        score_list.append(a)
        score_list = score_list[1:]
        i+=1
    else:
        break
stop = time()
print(i+1, stop-start)
