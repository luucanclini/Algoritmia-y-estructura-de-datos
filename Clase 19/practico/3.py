from ..arbol.arbol.LinkedTree import *

def funcion(A,R):
    for n in A.positions():
        if n.element() == R:
            camino = []
            camino.append(n.element())
            
            while not A.is_root(n):
                n = A.parent(n)
                camino.append(n.element())
            print (camino)
