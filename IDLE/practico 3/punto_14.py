from math import factorial,asin

def arcoseno(x,vueltas):
    sumatoria = 0
    for n in range(vueltas):
        numerador = factorial(2*n)
        denominador = (4**n)*((factorial(n))**2)*(2*n+1)
        mult = x**(2*n+1)
        sumatoria = (numerador/denominador)*mult
    return sumatoria

x = abs(int(input('ingrese un valor en grados: ')))
c = int(input('ingrese el nivel de aproximacion: '))

print('valor calculado con taylor:',arcoseno(x,c))
print('valor calculado con coseno:',asin(x))

