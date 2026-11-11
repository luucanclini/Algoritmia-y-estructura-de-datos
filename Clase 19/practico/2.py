#inorden postorden por niveles
from ..arbol.arbol.LinkedTree import *

import sys
import os

# Le agregamos a Python la carpeta exacta donde están ArrayStack y Empty
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Clase16/stack_queue/stack_queue")))

from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def postorden(T,v):
    for w in T.children(v):
        postorden(T,w)
    visitar(T,v)

def visitar(a,b):
    pass

def inorden(T,v):
    if T.is_leaf(v):
        visitar(T,v)
    else:
        hijos = T.children(v)
        i = 0
        w = hijos[i]

        inorden(T,w)
        visitar(T,v)

        while i + 1 < len(hijos):
            i += 1
            w = hijos[i]
            inorden(T,w)

def niveles(T):
    cola = ArrayQueue()
    cola.enqueue(T.root())
    cola.enqueue(None)

    while not cola.isEmpty():
        v = cola.dequeue()
        if v != None:
            print (v.element(),end=' ')
            for w in T.children(v):
                cola.enqueue(w)
        else:
            print('fin de linea')
            if not cola.isEmpty():
                cola.enqueue(None)