# No puedo referenciar abs porque esta
# en el entorno predefinido y
# el nuevo abs del programa principal
# la oculta.
# Idem print e input.

def abs(x):
    return 3*x

imprimir = print
leer = input
x = -9
y = abs(x)
print(y)

print = 8


imprimir("mama")
x = int(leer("Dame un entero:"))
