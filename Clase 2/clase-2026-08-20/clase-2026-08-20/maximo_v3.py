# Calcular el maximo entre a, b y c
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

if a > b and a > c:
    maximo = a
else:
    if b > c:
        maximo = b
    else:
        maximo = c

print(f"El maximo entre {a}, {b} y {c} es {maximo}")
