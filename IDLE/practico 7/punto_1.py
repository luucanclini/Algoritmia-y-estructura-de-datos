from math import sin,log

def f(x):
    numerador = 3*sin(5*x**2)
    denominador = x + 2
    valor = (numerador/denominador) + log(4*x)
    return valor

