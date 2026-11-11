def profundidad(T,v):
    if T.is_root(v):
        return 0
    else:
        return 1 + profundidad(T,T.parent(v))

def profundidadRotulo(A,R):
    for n in A.positions():
        if n.element() == R:
            return profundidad(A,n)