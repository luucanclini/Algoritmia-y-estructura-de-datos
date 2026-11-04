from math import sqrt

class EcuacionCuadratica():
    def __init__(self,a,b,c):
        if a == 0:
            raise Exception('a debe ser distinto de 0')
        self._a = a
        self._b = b
        self._c = c

    def __str__(self):
        return f'({self._a})x**2 + ({self._b})x + ({self._c})'

    def resolver(self):
        a = self._a
        b = self._b
        c = self._c

        discriminante = ((b)**2) - 4*a*c
        if discriminante<0:
            return f'({None},{None})'
        elif discriminante == 0:
            x = -b/(2*a)
            return (x,x)
        else:
            x1 = (-b-sqrt(discriminante))/(2*a)
            x2 = (-b+sqrt(discriminante))/(2*a)
            return (x1,x2)