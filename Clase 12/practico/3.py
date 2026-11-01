from math import sqrt

def ordenar(a,v):
    n = len(a)
    for i in range(n-1):
        p = i # asumo el mas pequeño p esta en i
        for j in range(i+1,n):
            if modulo(a[j], v) < modulo(a[p], v):
                p = j
        a[i], a[p] = a[p], a[i]
    return a

def modulo(a,b):
    modulo = sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
    return modulo
a = []
v = ()
a = ordenar(a,v)
print('punto mas cercano:', a[0])
print('punto mas lejano:', a[-1])
print('anteultimo punto mas lejano:', a[-2])