def mcd(a,b):
    cociente = a//b
    resto = a%b
    if resto != 0:
        resultado = mcd(b,resto)
    else:
        resultado = b
    return resultado

try:
    a = int(input("ingrese un valor para a:"))
    b = int(input("ingrese un valor para b:"))
    
    maximo = max(a,b)
    minimo = min(a,b)
    mcd = mcd(maximo,minimo)
    print('el maximo comun divisor entre:',maximo,'y',minimo,'es:',mcd)
except ValueError:
    print('solo se permiten numeros enteros')