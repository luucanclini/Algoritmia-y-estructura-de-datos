cadena = input("ingresa una palabra: ")

i = 0
j = len(cadena) - 1
palindromo = True

while i<j and palindromo:
    if cadena[i] != cadena[j]:
        palindromo = False
    i += 1
    j -= 1

m = 'la palabra '+cadena
if palindromo:
    print(m,'es un palindormo')
else:
    print(m,'no es un palindromo')