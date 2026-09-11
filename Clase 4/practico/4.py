n = abs(int(input('ingrese un valor para determinar si es primo: ')))
aparecio = False
termino = False

while not termino: 
    for i in range(2,n):
        if n%i == 0:
            aparecio = True

        if i == n-1 or aparecio == True:
            termino = True
if aparecio == True:
    print(n,'no es primo')
else:
    print(n,'es primo')
