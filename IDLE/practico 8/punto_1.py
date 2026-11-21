def suma(n):
    if n == 0:
        return 0
    elif n>0 :
        anterior = n-1
        valor = n + suma(anterior)
        return valor

a = int(input('ingrese un valor para hacer la suma recursiva: '))
print(suma(a))

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        valor = Fibonacci(n-1) + Fibonacci(n-2)
        return valor

b = int(input('ingrese un valor para fibonacci: '))
print(Fibonacci(b))
