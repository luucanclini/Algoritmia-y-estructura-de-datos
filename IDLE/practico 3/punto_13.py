from math import factorial,cos,radians

def CosTaylor(x,c):
    sumatoria = 0
    for n in range(c):
        numerador = (-1)**n
        denominador = factorial(2*n)
        fraccion = numerador/denominador
        mult = x**(2*n)
        sumatoria = sumatoria + fraccion*mult
    return sumatoria

x = int(input('ingrese los grados para calcular el coseno: '))
v = int(input('ingrese la cantidad de vueltas para aproximar con taylor: '))

print('valor calculado con taylor:',CosTaylor(x,v))
print('valor calculado con coseno:',cos(x))
