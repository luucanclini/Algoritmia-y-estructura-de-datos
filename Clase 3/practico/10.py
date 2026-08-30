from math import sqrt

n = int(input("ingrese la cantidad de componentes del vector: "))
suma = 0

for i in range(n):
    x = float(input("ingrese la componente: "))
    suma = suma + x**2

norma = sqrt(suma)
print("la norma euclidiana es:", norma)