n = int(input('ingrese un valor para n: '))
def suma(n):
    if n == 0:
        return n
    return n+suma(n-1)

print('sumatoria:', suma(n) )