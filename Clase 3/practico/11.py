from math import sqrt

n = int(input("cuantos numeros va a ingresar? (n): "))
suma = 0

for i in range(n):
    x = float(input("ingrese el valor de x: "))
    suma = suma + x

promedio = suma/n
print("el promedio de las x en total es:", promedio)