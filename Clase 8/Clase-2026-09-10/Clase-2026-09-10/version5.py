# factorial(n) = de acuerdo
# a definicion recursiva incorrecta
# porque no decrece el tamanio del problema

def factorial(n):
    print("Calculando n: ", n)
    if n==0:
        resultado = 1
    else:
        resultado =  n * factorial(n) // n
    print("resultado: ", resultado)
    return resultado



print("FACTORIAL(4):")
print("-------------")
print("fact(4): ", factorial(4))


