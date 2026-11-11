class BTNode:
    def __init__(self, element, parent, left, right):
        self._element = element
        self._parent = parent
        self._left = left
        self._right = right
    
    def setParent(self, parent):
        self._parent = parent
        
    def setElement(self, element):
        self._element = element
        
    def setLeft(self, left):
        self._left = left
    
    def setRight(self, right):
        self._right = right
        
    def getParent(self):
        return self._parent
        
    def getElement(self):
        return self._element
        
    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right
    
    def element(self):
        return self.getElement()
