from ..LinkedBinaryTree import *

pregunta1 = 'esta nervioso acerca de su dinero?'
pregunta2 = 'necesitara usar el dinero en los proximos 5 años?'
pregunta3 = 'esta dispuesto a aceptar riesgos para obtener mayores ganancias?'


respuesta1 = 'abra una caja de ahorros'
respuesta2 = 'cree un plazo fijo renovable mensualmente'
respuesta3 = 'invierta en bonos de la deuda externa'
respuesta4 = 'invierta en un portafolio de acciones diversificado'

A = LinkedBinaryTree()

r = A.add_root(pregunta1)

s1 = A.add_left(r,respuesta1)
n1 = A.add_right(r,pregunta2)

s2 = A.add_left(n1,respuesta2)
n2 = A.add_right(n1,pregunta3)

s3 = A.add_left(n2,respuesta3)
n3 = A.add_right(n2,respuesta4)

def consultarUsuario(T):
    actual = T.root()
    continuar = True

    while continuar == True:

        print("\n" + actual.element())

        if not T.has_left(actual) and not T.has_right(actual):
            print('adios')
            continuar = False
        else:
            op = input('ingrese su respuesta:')
            print('1)Si')
            print('2)No')
            actual = recorrerArbol(T, actual, op)

def recorrerArbol(T,v,opcion):
    if opcion == '1':
        v = T.left(v)
    if opcion == '2':
        v = T.right(v)
    
    return v.element()

consultarUsuario(A)


    