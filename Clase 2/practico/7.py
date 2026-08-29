#7. Resolver la ecuaci ́on lineal ax + b = c para x (leer a, b y c y calcular x).
from math import isclose
print('sea la ecuacion lineal ax + b = c buscaremos x')
a= float(input('ingrese un valor para a:'))
b= float(input('ingrese un valor para b:'))
c= float(input('ingrese un valor para c:'))

if isclose(a,0.0):
    print("a debe ser distinto de 0")
else:
    x = (c-b)/a
    print("x =", x)