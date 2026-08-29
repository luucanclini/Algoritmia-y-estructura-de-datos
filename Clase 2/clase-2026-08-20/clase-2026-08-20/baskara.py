from math import sqrt

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

delta = b**2 - 4 * a * c
if a == 0:
    print("No es ecuacion cuadratica")
elif delta < 0:
    print("No hay raices reales")
elif delta == 0:
    x = -b / (2*a)
    if x == 0.0: x = 0.0
    print(f"La unica solucion es {x}")
elif delta > 0:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print(f"Las dos raices son {x1} y {x2}")
