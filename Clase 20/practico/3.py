from ..LinkedBinaryTree import *

def Evaluar(A,v):
    if not A.has_left(v) and not A.has_right(v):
        return v.element()
    else:
        op = v.element()
        v1 = Evaluar(A,A.left(v))
        v2 = Evaluar(A,A.right(v))
        return aplicar(op,v1,v2)

def aplicar(op,a,b):
    resultado = None
    if op == '+':
        resultado = a + b
    elif op == '-':
        resultado = a - b
    elif op == '*':
        resultado = a * b
    elif op == '/':
        resultado = a / b
    return resultado