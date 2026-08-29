# Calcular la raiz cuadrada de un numero leido
# por teclado
from math import sqrt

nro = float(input("Ingrese numero: "))
if nro >= 0:
    raiz = sqrt(nro)
    print(f"La raiz de {nro} es {raiz}")
else:
    print("No calculo raices de negativos")
print("Adios")

    
