from math import sin,sqrt

def f(x,y,z):

    termino1 = 1/(x-5)
    termino2 = 2/((2*x)+(5*y))
    termino3 = 3/(sin(3*z))**2
    termino4 = sqrt(x+y+z)
    cuenta = termino1 + termino2 + termino3 - termino4
    return cuenta

def validarDominio(x, y, z):
    if x == 5:
        raise Exception("Error de dominio: x no puede ser 5 (división por cero).")
    if (2 * x) + (5 * y) == 0:
        raise Exception("Error de dominio: 2x + 5y no puede ser 0 (división por cero).")
    if abs(sin(3 * z)) < 1e-12:
        raise Exception("Error de dominio: sin(3z) es 0 (división por cero).")
    if (x + y + z) < 0:
        raise Exception("Error de dominio: x + y + z no puede ser negativo (raíz cuadrada real).")
    return f(x, y, z)

try:
    x = float(input("Ingrese x: "))
    y = float(input("Ingrese y: "))
    z = float(input("Ingrese z: "))
    resultado = validarDominio(x, y, z)
    print("El resultado de f(x, y, z) es:", resultado)
except Exception as error:
    print(error)

