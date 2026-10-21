from math import sin, log
t = int(input('ingrese un valor para calcular la funcion: '))

def f(t):
    numerador = 3*sin(5*((t)**2))
    denominador = t + 2
    fraccion = numerador/denominador
    funcion = fraccion +log(4*t)
    return funcion

print(f(t))