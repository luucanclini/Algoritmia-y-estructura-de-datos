from LinkedBinaryTree import *
# from BTNode import *
from BinaryTreeException import *


def listar_pre(arbol):
    pre( arbol, arbol.root() )
    print()

def pre( arbol, nodo ):
    print(nodo.element(), " ", end="")
    if arbol.has_left(nodo):
        pre(arbol, arbol.left(nodo))
    if arbol.has_right(nodo):
        pre(arbol, arbol.right(nodo))

def listar_in( arbol ):
    in2( arbol, arbol.root())

def in2( t, p ):
    print("(", end="")
    if t.has_left(p): in2( t, t.left(p) )
    print( p.element(), end="" )
    if t.has_right(p): in2( t, t.right(p) )
    print(")", end="")


ab = LinkedBinaryTree()
ab.add_root( "+" )
raiz = ab.root()
ndiv = ab.add_left( raiz, "/" )
npor = ab.add_right( raiz, "*" )
ab.add_left( ndiv, "10" )
ab.add_right( ndiv, "2" )
ab.add_left( npor, "4" )
ab.add_right( npor, "8" )

print("Preorden: ")
listar_pre(ab)
print("Inorder:")
listar_in(ab)
