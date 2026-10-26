n = int(input('ingrese un valor para n: '))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n
print(fibonacci(n))