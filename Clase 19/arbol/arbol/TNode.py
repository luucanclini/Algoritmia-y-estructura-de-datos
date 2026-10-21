class TNode:
    def __init__(self, element, parent):
        self._element = element
        self._parent = parent
        self._children = [] # Un nodo tiene una lista vacia de hijos
       
    def setParent(self, parent):
        self._parent = parent
        
    def setElement(self, element):
        self._element = element
        
    def getParent(self):
        return self._parent
       
        
    def getChildren(self):
        return self._children
    
    
    def element(self):
        return self._element
