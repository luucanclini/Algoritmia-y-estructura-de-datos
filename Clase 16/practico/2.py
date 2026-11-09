import sys
import os

# Le agregamos a Python la carpeta exacta donde están ArrayStack y Empty
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../stack_queue/stack_queue")))

from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def esta_balanceada(cadena):
    pila = ArrayStack()
    parejas = {')': '(', ']': '[', '}': '{'}

    for elemento in cadena:
        if elemento in "([{":
            pila.push(elemento)

        if elemento in ")]}":
            if len(pila) < 1:
                raise Exception('cadena mal formada, no hay caracter de apertura')

            caracter = pila.pop()

            if parejas[elemento] != caracter:
                raise Exception ('funcion mal balanceada')

    if len(pila) == 0:
        mensaje = 'ecuacion balanceada'
    else:
        mensaje = 'ecuacion mal balanceada, quedaron elementos sin cerrar'

    return mensaje

exp1 = '{[()]}'
exp2 = "{[()()]}"
exp3 = "({[]})"
exp4 = "{[(])}"
exp5 = "{[()}"
exp6 = "{[()]"

print(esta_balanceada(exp6))