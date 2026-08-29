# Calculadora rudimentaria
from math import max

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

print("MENU")
print("====")
print("1. suma")
print("2. resta")
print("3. producto")
print("4. division")
print("5. maximo")
opcion = int(input("Ingrese eleccion: "))

# Hago eco:
# print(a,b,opcion)
if opcion == 1:
    suma = a+b
    print(f"La suma es {suma}")
    print("La suma es ", a+b)
elif opcion == 2:
    resta = a-b
    print(f"La resta es {resta}")
elif opcion == 3:
    producto = a*b
    print(f"El producto es {producto}")
elif opcion == 4:
    if b != 0:
        division = a / b
        print(f"El cociente es {division}")
    else:
        print("No divido por cero")
elif opcion == 5:
    maximo = max(a,b)
    print(f"El maximo es {maximo}")
else:
# Otra opcion: elif opcion <= 0 or opcion >= 5:
    print("Opcion no contemplada por el sistema")
