from ..LinkedBinaryTree import *

def visitar():
    pass

def preorden(A,v):
    if pos is None:
        pos = []
    
    # 1. Visitar v PRIMERO (guardamos la posición v en la lista)[cite: 46]
    pos.append(v)

    if A.has_left(v):
        preorden(A,A.left(v))
    if A.has_right(v):
        preorden(A,A.right(v))

    return pos

def posorden(A,v):
    if A.has_left(v):
        posorden(A,A.left(v))
    if A.has_right(v):
        posorden(A,A.right(v)) 
    visitar(v)

def inorden(A,v):
    if A.has_left(v):
        inorden(A,A.left(v))
    visitar(v)
    if A.has_right(v):
        inorden(A,A.right(v)) 