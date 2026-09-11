n = abs(int(input("ingrese un numero natural para saber si es divisible por 9: ")))
numOriginal = n
sumatoria = 0
valor = 0
while True:
    if n>0:
        valor = n%10
        sumatoria = sumatoria + valor
        n = n//10
    else:
        break
    
if sumatoria == 9:
    print(numOriginal, 'es divisible por 9')
else:
    print(numOriginal,'no es divisible por 9')
        