from math import log10
a = int(input('ingrese el valor entero para a: '))
b = int(input('ahora el valor entero para b: '))
suma = a + b
resta = a - b
producto = a * b
cociente = a//b
resto = a%b
logaritmo = log10(a)
potencia = a**b
print(a,'+',b,' = ',suma)
print(a,'-',b,' = ', resta)
print(a,'x',b,' = ', producto)
print(a,':',b,' = ',cociente)
print('resto de',a,':',b,' = ',resto)
print('logaritmo de ',a,'en base 10 = ', logaritmo)
print(a,' a la ',b,' = ',potencia)