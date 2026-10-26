entero = int(input('ingrese un numero entero para hallar su inverso:'))

def invertir(num):
    inverso = 0
    while num > 0:
        inverso = inverso *10 + (num % 10)
        num = num//10
    return inverso

print('el inverso de',entero,'es',invertir(entero))