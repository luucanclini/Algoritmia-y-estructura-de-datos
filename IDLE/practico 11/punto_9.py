def filas(a):
    return len(a)

def columnas(a):
    return len(a[0])


def suma_matrices(a,b):
    if columnas(a)!=columnas(b):
        raise Exception('para sumar matrices deben tener la misma cantidad de columnas')
    elif filas(a)!=filas(b):
        raise Exception('para sumar matrices deben tener la misma cantidad de filas')
    for i in range(filas(a)):
        for j in range(columnas(a)):
            a[i][j] = a[i][j] + b[i][j]

    return a

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

try:
 print(suma_matrices(a,c))
except Exception as error:
    print("Excepción capturada:", error)
