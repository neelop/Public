# 9^5 = 59049
# 6 digits - 6*9^5 =354294
# 7 digits - 7*9^5 = 413343 ==> 6 digit number ==> number cannot be higher than 6*9^5

limit = 6 * 9 ** 5

score = 0
for i in range(2, limit + 1):
    k = str(i)
    sum_1 = 0
    for j in k:
        sum_1 += int(j) ** 5
    if sum_1 == i:
        score += i
print(score)