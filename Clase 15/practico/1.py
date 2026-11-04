class Fraccion():
    
    def __init__(self,numerador,denominador):
        
        if denominador == 0:
                    raise Exception('no se puede dividir por 0')
        
        self._numerador = numerador
        self._denominador = denominador


    def set_numerador(self,numerador):
        self._numerador = numerador
    def set_denominador(self,denominador):
        self._denominador = denominador


    def get_numerador(self):
        return self._numerador
    def get_denominador(self):
        return self._denominador


    def __str__(self):
        return f'{self._numerador}/{self._denominador}'
    def __repr__(self):
        return f'Fraccion({self._numerador},{self._denominador})'

    
    def get_numero(self):
        return self._numerador/self._denominador
    
    def suma(self,other):
        nuevoNumerador = (self._numerador*other._denominador)+(other._numerador*self._denominador)
        nuevoDenominador = (self._denominador*other._denominador)
        return Fraccion(nuevoNumerador,nuevoDenominador)

    def producto(self,other):
        n = self._numerador*other._numerador
        d= self._denominador*other._denominador
        return Fraccion(n,d)
    def division(self,other):
        n=self._numerador*other._denominador
        d=self._denominador*other._numerador
        return Fraccion(n,d)

f1 = Fraccion(1,2)
f2 = Fraccion(3,4)

f3=f1.suma(f2)
f4=f1.producto(f2)
f5=f1.division(f2)

print(f'suma: {str(f3)},producto: {str(f4)},division: {str(f5)}')