lista1 = ['John', 'Paul', 'George', 'Ringo']
elem = lista1[2]
print("lista: ", lista1)
print("elemento: ", elem)
print("Elementos de a uno:")
for x in lista1:
    print(x)
print("Otra forma:")
n = len(lista1)
for i in range(n):
    x = lista1[i]
    print(x)
print()
cadena = input("Ingrese lista de numeros separados por blanco:")
print("La cadena es ", cadena)
lista_subcadenas = cadena.split(" ")
print("Lista de subcadenas: ", lista_subcadenas)

lista_nros = [56, 78, 45]
print("Lista de nros: ", lista_nros)
ult = lista_nros[ len(lista_nros)-1 ]
print("Ultimo: ", ult)
ult = lista_nros[-1]
print("Ultimo: ", ult)
ante_ult = lista_nros[-2]
print("Ante ultimo ultimo: ", ante_ult)
lista_nros.insert( 2, 666 )
print("Lista de nros: ", lista_nros)
lista_nros.insert( len(lista_nros), 9999 )
print("Lista de nros: ", lista_nros)

lista_nros.append( 88888888 )
print("Lista de nros: ", lista_nros)

# Conversion de la lista de subcadenas en la lista de numeros
resultado = []
for nro in lista_subcadenas:
    resultado.append( int(nro) )
print("Resultado: ", resultado)

print("Vamos a borrar el 78:")
lista_nros.remove(78)
print("Lista de numeros: ", lista_nros)

print("Eliminemos el elemento en la posicion 2:")
lista_nros.pop(2)
print("Lista de numeros: ", lista_nros)
print("Elimino el ultimo:")
lista_nros.pop()
print("Lista de numeros: ", lista_nros)
print("Limpiemos la lista:")
lista_nros.clear()
print("Lista de numeros: ", lista_nros)

lista2 = [34, 12, 67, 89, 45, 23, 56]
print("Lista2: ", lista2)
lista2.sort()
print("Lista2: ", lista2)
lista2.reverse()
print("Lista2: ", lista2)




































