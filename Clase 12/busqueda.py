def buscar_lineal(a, x):
    n = len(a)
    for i in range(n):
        #print(i)
        if x == a[i]:
            return i
    return -1

def buscar_binaria(a, x):
    ini = 0
    fin = len(a)-1
    while ini <= fin:
        medio = (ini+fin) // 2
        #print(ini, fin, medio)
        if x == a[medio]: return medio
        elif x < a[medio]: fin=medio-1
        else: ini=medio+1
    return -1

def ordenar(a):
    n = len(a)
    for i in range(n-1):
        p = i # asumo el mas pequeño p esta en i
        for j in range(i+1,n):
            if a[j] < a[p]: p = j
        a[i], a[p] = a[p], a[i]
        
def buscar_matriz(m, item):
    filas = len(m)
    cols = len(m[0])
    for i in range(filas):
        for j in range(cols):
            if item == m[i][j]:
                return (i,j)
    return None


#----------- main --------
matriz = [ [1,3,4], [5,6,9] ]
par = buscar_matriz( matriz, 6 )
print("par: ", par)

'''
lista = []
for x in range(1000000):
    lista.append(x**2)
pos = buscar_lineal(lista, 99)
print("pos: ", pos)

pos = buscar_binaria(lista, 625)
print("pos: ", pos)

lista2 = [34, 56, 78, 90]
pos = buscar_binaria(lista2, 625)
print("pos: ", pos)

lista3 = [34, 1, 56, 6, 7, 12, 56, 788, 3, 456]
print("lista desordenada: ", lista3)
ordenar(lista3)
print("lista ordenada   : ", lista3)
'''








