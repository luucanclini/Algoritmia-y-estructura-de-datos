from math import cos,factorial
x = int(input('ingrese un valor para x: '))
#vamos a acotar el infinito
infinito=100
coseno = cos(x)
sumatoria=0
for n in range(infinito):
    numerador=(-1)**n
    denominador=factorial(2*n)
    x1= x**(2*n)
    valor=(numerador/denominador)*x1
    sumatoria=sumatoria+valor

print(coseno,'=',sumatoria)
