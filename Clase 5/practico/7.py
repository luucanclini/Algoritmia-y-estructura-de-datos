from math import sqrt
v = (1,4,9,3,8)
modulo = 0
i=0
while i<5:
    modulo = modulo + (v[i])**2
    i += 1

modulo = sqrt(modulo)
print(modulo)
