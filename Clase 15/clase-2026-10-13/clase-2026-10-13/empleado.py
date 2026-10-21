from persona import Persona

class Empleado(Persona):
    def __init__(self, n, p, s):
        super().__init__(n, p)
        self._sueldo = s
        self._lugar_trabajo = None
    
    def get_sueldo(self):
        return self._sueldo

    def set_sueldo(self, nuevo_sueldo):
        self._sueldo = nuevo_sueldo

    def set_lugar_trabajo(self, f):
        self._lugar_trabajo = f
        
    def __str__(self):
        antes = super().__str__()
        return antes + " y gano " + \
               str(self.get_sueldo())

    
