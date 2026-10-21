class Persona:
    def __init__(self, n, p): # constructor
        if p <= 0:
            raise Exception("Peso negativo")
        self._nombre = n
        self._peso = p

    def get_nombre(self):
        return self._nombre

    def get_peso(self):  # consulta
        return self._peso

    def set_peso(self, nuevo_peso): # comando
        if nuevo_peso <= 0:
            raise Exception("Peso imposible")
        self._peso = nuevo_peso

    def engordar(self):
        self._peso *= 1.1

    def __str__(self):
        return f"Me llamo " + \
               f"{self._nombre} " + \
               f"y peso {self._peso} kg"
    
        
