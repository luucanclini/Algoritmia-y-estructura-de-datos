from math import asin,factorial
x = float(input('ingrese un valor para x: '))
#vamos a acotar el infinito
infinito=100
arcoseno = asin(x)
sumatoria=0
for n in range(infinito):
    numerador=factorial(2*n)
    denominador=(4**n)*((factorial(n))**2)*((2*n)+1)
    x1= x**(2*n+1)
    valor=(numerador/denominador)*x1
    sumatoria=sumatoria+valor

print(arcoseno,'=',sumatoria)
