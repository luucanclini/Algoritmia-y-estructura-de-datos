# factorial(n) = de acuerdo
# a definicion recursiva

def factorial(n):
    print("Calculando n: ", n)
    if n==0:
        resultado = 1
    else:
        resultado =  n * factorial(n-1)
    print("resultado: ", resultado)
    return resultado

print("FACTORIAL(0):")
print("-------------")
print("fact(0): ", factorial(0))

print("FACTORIAL(1):")
print("-------------")
print("fact(1): ", factorial(1))

print("FACTORIAL(4):")
print("-------------")
print("fact(4): ", factorial(4))

print("FACTORIAL(9):")
print("-------------")
print("fact(9): ", factorial(9))
#print("fact(300): ", factorial(300))
