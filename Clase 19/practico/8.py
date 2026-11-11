
def guardarProfundidad(T,v):

    profundidad = []
    profundidad.append(v)

    while v != T.root():
        v = T.parent(v)
        profundidad.append(v)

    return profundidad

def profundidadRotulo(A,R):
    for n in A.positions():
        if n.element() == R:
            return guardarProfundidad(A,n)

def ACMC(A,R1,R2):
    c1 = profundidadRotulo(A,R1)
    c2 = profundidadRotulo(A,R2)

    for n in c1:
        for n2 in c2:
            if n == n2:
                return n.element()


