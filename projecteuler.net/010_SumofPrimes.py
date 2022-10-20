from toolsy_sroolsy import isPrime

primesy = [2]
k = 1

while k < 2000000:
    if isPrime(k):
        primesy.append(k)
    k+=2

score = 0
for item in primesy:
    score+= item

print(score)