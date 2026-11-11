from ..LinkedBinaryTree import *
from recorrer import *

def positions(A):
    if A.is_empty():
        return []
    return preorden(A, A.root())

def Altura(A,n):
    if not A.has_left(n) and not A.has_right(n):
        return 0
    
    alt_izq = 0
    if A.has_left(n):
        alt_izq = Altura(A, A.left(n))
        
    alt_der = 0
    if A.has_right(n):
        alt_der = Altura(A, A.right(n))
        
    return 1 + max(alt_izq, alt_der)

def obtenerNodo(A,R):
    nodos = []
    for n in A.position():
        if n.element() == R:
            nodos.append(n)
