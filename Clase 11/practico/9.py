def cantFilas(a):
    return len(a)
def cantColumnas(a):
    return len(a[0])

def crearMatrizNula(a):
    matriz = [[0 for j in range(cantColumnas(a))] for i in range(cantFilas(a))]
    return matriz

def sumaMatrices(a,b):
    if cantFilas(a)!=cantFilas(b) or cantColumnas(a)!=cantColumnas(b):
        raise ValueError('las matrices deben tener la misma cantidad de filas y columnas')

    matriz = crearMatrizNula(a)

    for i in range(cantFilas(a)):
        for j in range(cantColumnas(a)):
            matriz[i][j] = a[i][j]+b[i][j]

    return matriz