def matrizNula(n,m):
    return [[0 for j in range(m)]for i in range(n)]

def matriz_traspuesta(a):
    n = filas(a)
    m = columnas(a)
    b = matrizNula(m,n)

    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]

    return b
    
def filas(a):
    return len(a)

def columnas(a):
    return len(a[0])

a = [
    [1, 4, -2],
    [4, 5, 8],
    [-2, 8, 0],
]

b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

c = [
    [1, 2, 3],
    [4, 5, 6],
]

print(matriz_traspuesta(c))
