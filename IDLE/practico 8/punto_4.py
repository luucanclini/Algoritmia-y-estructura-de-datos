def suma(n,m):
    if m == 0:
        return n
    else:
        return succ(suma(n,pred(m)))

def producto(n,m):
    if m == 0:
        return 0
    else:
        return suma(producto(n,pred(m)),n)

def pred(n):
    return n-1
def succ(n):
    return n+1

