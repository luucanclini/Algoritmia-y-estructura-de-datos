from math import log10

numero = int(input("Ingrese un numero entero: "))
numero = abs(numero)
if numero == 0: cantidad_digitos = 0
else: cantidad_digitos = int(log10(numero)) + 1
print("cantidad digitos: ", cantidad_digitos)

for i in range(cantidad_digitos):
    digito = numero % 10
    print(digito)
    numero = numero // 10

print("Adios")


