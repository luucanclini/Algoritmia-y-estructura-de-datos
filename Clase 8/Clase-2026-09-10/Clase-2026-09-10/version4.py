# factorial(n) = de acuerdo
# a definicion recursiva
# Me olvide de programar el caso base

def factorial(n):
    print("Calculando n: ", n)
    resultado =  n * factorial(n-1)
    print("resultado: ", resultado)
    return resultado


print("FACTORIAL(4):")
print("-------------")
print("fact(4): ", factorial(4))
