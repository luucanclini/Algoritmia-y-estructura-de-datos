import sys
import os

# Le agregamos a Python la carpeta exacta donde están ArrayStack y Empty
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../stack_queue/stack_queue")))

from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue
pila = ArrayStack()
def evaluar(expr):
    for elemento in expr:

        if elemento.isnumeric():
            pila.push(float(elemento))

        if elemento in '+-/*':
            if len(pila)<2:
                raise Exception('expresion invalida')

            num2 = pila.pop()
            num1 = pila.pop()

            if elemento == '+':
                valor = num1 + num2
            elif elemento == '-':
                valor = num1 - num2
            elif elemento == '*':
                valor = num1 * num2
            elif elemento == '/':
                valor = num1 / num2

            pila.push(valor)
    if pila != 1:
        raise Exception('expresion invalida, quedaron elementos sin operar')

    return pila.pop()

exp1 = ['2', '3', '+', '4', '1', '-', '*'] # Tiene que dar 15
exp2 = ['5', '2', '+', '3', '/']            # Tiene que dar 2.33333
exp3 = ['*', '2', '3', '*', '+']            
exp4 = ['4', '5', '+', '6']

print(evaluar(exp3))
