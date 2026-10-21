from Empty import Empty

class ListQueue:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        """Agrega un elemento a la cola."""
        self.elementos.append(elemento)

    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola.
            Si la cola está vacía, lanza una Empty exception."""
        if self.is_empty():
            raise Empty("Cola vacía")
        return self.elementos.pop(0)

    def first(self):
        """Devuelve el primer elemento de la cola.
        Si la cola está vacía, lanza una Empty exception."""
        if self.is_empty():
            raise Empty("Cola vacía")
        return self.elementos[0]

    def is_empty(self):
        """Devuelve True si la cola está vacía, False de lo contrario."""
        return len(self.elementos) == 0

    def __len__(self):
        """Devuelve el número de elementos en la cola."""
        return len(self.elementos)
