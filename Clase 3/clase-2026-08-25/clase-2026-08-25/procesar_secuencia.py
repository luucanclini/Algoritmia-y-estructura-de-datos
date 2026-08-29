from math import inf
n = int(input("Ingrese largo: "))

suma = 0
maximo = -inf
contador = 0
for i in range(n):
    x = float(input(f"Ingrese numero {i+1} de {n}: "))
    suma += x
    if x > maximo: maximo = x
    if x == 8: contador = contador + 1
    
print("Fin")

print("La suma es ", suma)
if n > 0:
    print("El unico numero que recuerdo es ", x)
    promedio = suma / n
    print("Promedio: ", promedio)
    print("Maximo: ", maximo)
    print("La cantidad de 8s es ", contador)
else:
    print("No hay promedio ni maximo")

'''
n   |  i  |   x   |  suma  | maximo
-----------------------------------
4                     0       -1
4      0      10      10      10
4      1       8      18      10
4      2       6      24      10 
4      3       9      35      10

promedio = 33 / 4 = 8.25

Para probar maximo hay que ver que ocurre
cuando la secuencia es vacia,
el maximo es el primero,
el maximo esta en el medio, y
el maximo es el ultimo.

'''
