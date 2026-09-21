lista = [10, 20, 40, 50]
valor = int(input('ingrse un valor: '))

#opcion 1
"""
if valor <= lista[0]:
    lista.insert(0,valor)
elif valor >= lista[-1]:
    lista.append(valor)
else:
    for i in range(len(lista)):
        num1=lista[i]
        if num1 >= valor:
            lista.insert(i,valor)
            break

print('nueva lista ordenada: ', lista)
"""

#opcion 2

lista.append(valor)
lista.sort()

print('nueva lista ordenada: ', lista)