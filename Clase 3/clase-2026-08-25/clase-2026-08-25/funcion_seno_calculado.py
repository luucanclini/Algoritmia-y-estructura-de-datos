from math import factorial, sin

x = float(input("Ingrese x: "))
vueltas = 70
suma = 0.0
for n in range(vueltas):
    dosnmas1 = 2*n+1
    numerador = ((-1)**n) * (x ** dosnmas1)
    denominador = factorial(dosnmas1)
    termino = numerador / denominador
    suma += termino

print("El seno calculado es : ", suma)
print("El seno de math es   : ", sin(x))
error = abs(suma-sin(x))
print("Error: ", error)
