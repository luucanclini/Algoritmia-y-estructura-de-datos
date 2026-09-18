cadena = 'Dabale arroz a la zorra el abad'
cadenaMod = (cadena.upper()).replace(' ','')

i = 0
j = len(cadenaMod) - 1
palindromo = True

while i<j and palindromo:
    if cadenaMod[i] != cadenaMod[j]:
        palindromo = False
    i += 1
    j -= 1

m = 'la frase '+cadena
if palindromo:
    print(m,'es un palindormo')
else:
    print(m,'no es un palindromo')