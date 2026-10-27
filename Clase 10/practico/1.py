def leerNum():
    numero = input('ingrese un numero: ')
    return numero

def esPar(numero):
    cifra = numero[0]
    par = False
    num = int(cifra)
    if num%2 == 0:
        par = True
    return par

def calculo(valor,paridad):
    sumatoria = 0
    multiplicidad = 1
    if paridad:
        for num in valor:
            sumatoria = int(num) + sumatoria
            resultado = sumatoria
    else:
        for num in valor:
            multiplicidad = int(num) * multiplicidad
            resultado = multiplicidad
    return resultado



numero = leerNum()
par = esPar(numero)
valor =calculo(numero,par)
if esPar:
    print('sumatoria: ', valor)
else:
    print('producto: ', valor)