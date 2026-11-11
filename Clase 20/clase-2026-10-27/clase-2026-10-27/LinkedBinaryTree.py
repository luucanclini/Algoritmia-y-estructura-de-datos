from BTNode import *
from BinaryTreeException import *

class LinkedBinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size
        
    def add_root(self, element):
        if self._root != None:
            raise BinaryTreeException("El arbol ya tiene raiz")
        self._root = BTNode(element, None, None, None)
        self._size = 1
        
    def is_empty(self):
        return self._root == None
    
    def root(self):
        if self.is_empty():
            raise BinaryTreeException("El arbol esta vacio")
        return self._root
    
    def is_root(self, p):
        return p.getParent() == None
    
    def has_left(self, p):
        return p.getLeft() != None
        
    def has_right(self, p):
        return p.getRight() != None
        
    def parent(self, p):
        if self.is_root(p):
            raise BinaryTreeException("La posicion no tiene padre: p" + str(p.element()))
        return p.getParent()
    
    def left(self, p):
        if not self.has_left(p):
            raise BinaryTreeException("La posicion no tiene hijo izquierdo: p" + str(p.element()))
        return p.getLeft()
        
    def right(self, p):
        if not self.has_right(p):
            raise BinaryTreeException("La posicion no tiene hijo derecho: p: " + str(p.element()))
        return p.getRight()
    
    def add_left(self, p, element):
        if self.has_left(p):
            raise BinaryTreeException("La posicion ya tiene hijo izquierdo: p: " + str(p.element()))
        nodo = BTNode(element, p, None, None)
        p.setLeft(nodo)
        self._size += 1
        return nodo
    
    def add_right(self, p, element):
        if self.has_right(p):
            raise BinaryTreeException("La posicion ya tiene hijo derecho: p: " + str(p.element()))
        nodo = BTNode(element, p, None, None)
        p.setRight(nodo)
        self._size += 1
        return nodo
        
    def attach(self, p, t1, t2):
        if self.has_left(p):
            raise BinaryTreeException("La posicion ya tiene hijo izquierdo: p: " + str(p.element()))
        if self.has_right(p):
            raise BinaryTreeException("La posicion ya tiene hijo derecho: p: " + str(p.element()))
        p.setLeft( t1.root() )
        p.getLeft().setParent( p )
        p.setRight( t2.root() )
        p.getRight().setParent( p )
        self._size += len(t1) + len(t2)