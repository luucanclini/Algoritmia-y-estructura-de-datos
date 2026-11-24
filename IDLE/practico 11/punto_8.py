def filas(a):
    return len(a)

def columnas(a):
    return len(a[0])

def es_matriz_simetrica(a):
    esSimetrica = True
    if filas(a)!= columnas(a):
        raise Exception('la matriz debe ser cuadrada')
    
    for i in range(filas(a)):
        for j in range(columnas(a)):
            if a[i][j] != a[j][i]:
                return False
    return esSimetrica

simetrica = [
    [1, 4, -2],
    [4, 5, 8],
    [-2, 8, 0],
]

no_simetrica = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

no_cuadrada = [
    [1, 2, 3],
    [4, 5, 6],
]

print("Simétrica:", es_matriz_simetrica(simetrica))        # True
print("No simétrica:", es_matriz_simetrica(no_simetrica))  # False

try:
    print("No cuadrada:", es_matriz_simetrica(no_cuadrada))
except Exception as error:
    print("Excepción capturada:", error)
