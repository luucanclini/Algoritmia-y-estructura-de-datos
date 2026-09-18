cadena = str(input("ingrese una cadena: ")).lower()

countVocales = 0
vocales = ('a','e','i','o','u')

for c in cadena:
    if c in (vocales):
        countVocales = countVocales + 1
print(cadena,'tiene',countVocales,'vocales')
