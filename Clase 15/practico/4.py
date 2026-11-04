from math import sqrt
from ej3 import *

class Poligono():
    def __init__(self):
        self._puntos = []

    def insertarPunto(self,p):
        self._puntos.append(p)

    def __str__(self):
        return f'{self._puntos}'

    def perimetro(self,lista):
        sumatoria = 0
        
        for i in range(len(self._puntos) - 1):
            sumatoria += self._puntos[i].distancia(self._puntos[i+1])
            
        sumatoria += self._puntos[-1].distancia(self._puntos[0])
        return sumatoria
