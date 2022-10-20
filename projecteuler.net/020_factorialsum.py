number = 1
for i in range(1, 101):
    number = number * i
    while number % 10 == 0:
        number = int(str(number)[:-1])
asum = 0
for item in str(number):
    asum += int(item)
print(asum)