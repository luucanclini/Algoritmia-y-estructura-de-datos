from TNode import *
from TreeException import *

class LinkedTree:
    
    def __init__(self):
        self._tamano = 0
        self._raiz = None
        
    def create_root(self, r):
        if self.root() != None:
            raise TreeException("Ya tiene raiz")
        self._raiz = TNode(r, None)
        self._tamano = 1
    
    def add_last_child(self, p, e):
        nodo_nuevo = TNode(e, p)
        p.getChildren().append(nodo_nuevo)
        self._tamano += 1
        return nodo_nuevo

    def root(self):
        return self._raiz
 
    def is_root( self, p ):
        return self._raiz == p

    def parent( self, p ):
        return p.getParent()

    def num_children( self, p ):
        return len(p.getChildren())

    def children( self, p ):
        return p.getChildren()

    def is_leaf( self, p ):
        return len(p.getChildren()) == 0

    def __len__( self ):
        return self._tamano

    def is_empty( self ):
        return self._raiz == None

    def replace( self, p, elem ):
        valor_viejo = p.element()
        p.setElement(elem)
        return valor_viejo

    def preorder(self):
        if not self.is_empty( ):
            for p in self._subtree_preorder(self.root()): 
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p): 
           for other in self._subtree_preorder(c): 
               yield other 
            
    def positions(self):
        return self.preorder( )

    def __iter__(self):
        for p in self.positions( ): 
            yield p.element( )   
        
