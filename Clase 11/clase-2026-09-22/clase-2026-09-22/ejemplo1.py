def cant_filas(m):
    return len(m)

def cant_cols(m):
    return len(m[0])

def imprimir_matriz(m):
    filas = cant_filas(m)
    cols = cant_cols(m)
    for i in range(filas):
        print("|", end='')
        for j in range(cols):
            x = m[i][j]
            print("%10i"%(x), end='')
        print('|')

def det2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def crear_matriz(filas, cols):
    return [ [0 for j in range(cols)] \
             for i in range(filas)]

def producto_por_escalar(k, a):
    filas = cant_filas(a)
    cols = cant_cols(a)
    resultado = crear_matriz(filas, cols)
    for i in range(filas):
        for j in range(cols):
            resultado[i][j] = k * a[i][j]
    return resultado


def producto_matricial(a, b):
    m = cant_filas(a)
    n = cant_cols(a)
    n2 = cant_filas(b)
    p = cant_cols(b)
    if n != n2: raise Exception("Dimensiones mal")
    c = crear_matriz(m, p)
    # completar
    for i in range(m):
        for j in range(p):
            # Hago producto escalar de fila i por col j
            # usando k para recorrer y acumular en c[i][j]
            c[i][j] = 0
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

# ------- main --------------
a = [[23,12], [3,74]]
d = det2(a)
print("determinante: ", d)
filas = cant_filas(a)
print("filas:    ", filas)
print("columnas: ", cant_cols(a))
print("a:", a)
imprimir_matriz(a)

b = crear_matriz(2,3)
print("b: ")
imprimir_matriz(b)
b[1][2]=7
print("b modificada:")
imprimir_matriz(b)
c = producto_por_escalar(10, a)
print("10*a:")
imprimir_matriz(c)

a = [ [1,2,0], [-3,1,4]]
b = [ [0,1,-5,3], [2,1,0,-2], [7,5,-2,10]]
c = producto_matricial(a, b)
print("a:"); imprimir_matriz(a)
print("b:"); imprimir_matriz(b)
print("c:"); imprimir_matriz(c)







