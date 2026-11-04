from math import sqrt

class Punto2D():
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def distancia(self, p):
        modulo = sqrt(((self._x - p._x)**2)+(self._y - p._y)**2)
        return modulo

