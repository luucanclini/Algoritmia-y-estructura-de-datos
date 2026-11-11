'''
((3-1) + (2*4)) expresada como árbol:
       (+)
      /   \
    (-)   (*)
   /  \   / \
 (3) (1) (2) (4)
'''
from LinkedBinaryTree import *


def inorder(t):
    inorder_aux(t, t.root())
    print()

def inorder_aux(t, p):
    print( "(", end="" )
    if t.has_left(p):
        inorder_aux( t, t.left(p) )
    print( p.element(), end= "" )
    if t.has_right(p):
        inorder_aux( t, t.right(p) )
    print( ")", end="" )


arbol = LinkedBinaryTree()
print("arbol.is_empty(): ", arbol.is_empty())

arbol.add_root( '+' )
print("arbol.is_empty(): ", arbol.is_empty())

raiz = arbol.root()
print( "raiz: ", raiz.element() )

p_menos = arbol.add_left( raiz, '-' )
p_por = arbol.add_right( raiz, '*' )
arbol.add_left( p_menos, '3' )
arbol.add_right( p_menos, '1' )
arbol.add_left( p_por, '2' )
p_cuatro = arbol.add_right( p_por, '4' )

print( "arbol: ", end='' )
inorder(arbol)

otro_arbol = LinkedBinaryTree()
otro_arbol.add_root( '+' )
r = otro_arbol.root()
otro_arbol.add_left( r, '7' )
otro_arbol.add_right( r, '9' )
print( 'otro arbol: ', end='' )
inorder( otro_arbol )

arbol_grande = LinkedBinaryTree()
arbol_grande.add_root( '*' )
rag = arbol_grande.root()
arbol_grande.attach( rag, arbol, otro_arbol )
print( "arbol_grande: ", end='')
inorder( arbol_grande )
