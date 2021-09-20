f = open("p022_names.txt", "r")
names = ''
for x in f:
    names += (x)
names = names.replace('"', '')
list_of_names = names.split(",")
list_of_names.sort()

i = 1
sum1 = 0

for name in list_of_names:
    sum2 = 0
    for letter in name:
        sum2 += ord(letter) - 64
    sum1 += sum2 * i
    i += 1
print(sum1)
