#primitive bruteforce
sumquare = 0
for item in range(1,101):
    b = item*item
    sumquare += b
squaresum = 0
for item in range(1,101):
    squaresum += item

squaresum = squaresum*squaresum

print(squaresum - sumquare)