def suma(a,b,c,d):
    if b == 0:
        raise Exception('b debe ser distinto de 0')
    if d == 0:
        raise Exception('d debe ser distinto de 0')
    numerador = (a*d)+(b*c)
    denominador = b*d
    r = mcd(numerador,denominador)
    numerador = numerador//r
    denominador = denominador//r
    return (numerador,'/',denominador)
    

    
def mcd(a,b):
    if not isinstance(a, int) or isinstance(a, bool):
        raise Exception("el valor A debe ser de tipo entero")
    if not isinstance(b, int) or isinstance(b, bool):
        raise Exception("el valor B debe ser de tipo entero")
    
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        r = a%b
        return mcd(b,r)

try:
    print('ingrese los valores para las fracciones de la siguiente forma: a/b c/d')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    d = int(input('d: '))
    f1 = a/b
    f2 = c/d
    print(suma(a,b,c,d))
except ZeroDivisionError:
    print('no se puede dividir por cero')
