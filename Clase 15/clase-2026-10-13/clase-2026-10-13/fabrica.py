class Fabrica:
    def __init__(self, nombre, direccion):
        self._nombre = nombre
        self._direccion = direccion

    def __str__(self):
        return f"Fabrica: {self._nombre} en {self._direccion}"
