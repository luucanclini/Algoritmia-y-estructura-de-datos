from stack_queue.stack_queue.ArrayStack import ArrayStack

pila = ArrayStack()
def evaluar(expr):
    for elemento in expr:
        if elemento in '+-/*':
            if len(pila)<2:
                raise Exception('expresion invalida')
        if elemento.isnumeric():
            pila.push(float(elemento))
            
