

# a+ b + c == 1000
# a^2 + b^2 == c^2

# c == 1000 - a - b
# a^2 + b^2 == (1000 - a - b)^2


counter = 0
a = 1
b = 1
while a ** 2 + b**2 != (1000-a-b) ** 2:
     a+=1
     if a == 1000:
         a=1
         b+=1
print(a*b*(1000-a-b))