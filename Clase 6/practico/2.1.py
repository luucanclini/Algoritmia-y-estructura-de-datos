lista = [34, 27, 45, 45, 27, 34]
lista2 = lista.copy()
lista2.reverse()

if lista == lista2:
    print(lista, 'es palindromo')
else:
    print(lista, 'no es palindromo')