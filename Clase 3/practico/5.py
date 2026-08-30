from math import sin
n = int(input('cuantos numeros desea ingresar en el conjunto S?: '))
contador=0
for i in range(1,n+1):
    a = float(input('ingrese el valor: '))
    if 0.5<=sin(a)<=1.0:
        contador = contador+1
print(contador, 'cumplen con 0,5 ≤sin(xi) ≤1,0')