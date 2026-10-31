def cantFilas(a):
    return len(a)
def cantColumnas(a):
    return len(a[0])

def crearMatrizNula(a):
    matriz = [[0 for j in range(cantFilas(a))] for i in range(cantColumnas(a))]
    return matriz

def matrizTraspuesta(a):
    m = crearMatrizNula(a)
    for i in range(cantFilas(a)):
        for j in range(cantColumnas(a)):
            m[j][i] = a[i][j]
    return m