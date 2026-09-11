from math import sqrt
x = abs(int(input("ingrese un valor para calcular su raiz cuadrada: ")))
rta = x / 2

while abs((rta * rta) - x) >= 10**-7:
    rta = (rta + (x / rta)) / 2

print('Tu aproximación de la raíz es:', rta)
print('La raíz usando math.sqrt es:', sqrt(x))