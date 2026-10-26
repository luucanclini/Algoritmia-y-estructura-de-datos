def reverse(s:list):
    if len(s) == 0:
        return []
    
    return reverse(s[1:]) + [s[0]]

palabra = 'hola'
lista = []
for i in palabra:
    lista.append(i)

print (reverse(lista))
