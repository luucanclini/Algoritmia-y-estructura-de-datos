#1. Calcular superficie y perimetro de un circulo de radio r pero validando que r sea positivo.
from math import pi
r=float(input('ingrese el radio del circulo para calcular su superficie y permimetro: '))
if r<0:
    print('debe ingresar un numero positivo')
else:
    superficie = pi*(r**2)
    perimetro = 2*pi*r
    print('superficie: ',superficie,'perimetro: ',perimetro)