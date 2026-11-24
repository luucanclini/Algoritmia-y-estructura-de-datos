def mcd(a,b):
    if not a is int:
        raise Exception('el valor A debe ser de tipo entero')
    if not b is int:
        raise Exception('el valor B debe ser de tipo entero')
    
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        r = a%b
        return mcd(b,r)

try:
    print('hallaremos el maximo comun divisor entre a y b')
    a = int(input('ingrese un valor para A:'))
    b = int(input('ingrese un valor para B:'))

    if a<b:
        aux = b
        b = a
        a = aux
    
    print(mcd(a,b))
except ValueError:
    print('Los valores ingresados deben ser de tipo entero')
