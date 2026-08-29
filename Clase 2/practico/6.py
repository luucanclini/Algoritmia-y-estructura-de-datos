#6. Dados 3 valores a, b, c determinar el m ́aximo, el m ́ınimo y el valor del medio. Nota: El valor del
#medio se puede obtener como a + b + c −maximo −minimo
a= float(input('ingrese un valor para a:'))
b= float(input('ingrese un valor para b:'))
c= float(input('ingrese un valor para c:'))

maximo=(max(a,(max(b,c))))
minimo=(min(a,(min(b,c))))
medio = a+b+c-maximo-minimo

print('maximo =',maximo,'minimo =',minimo,'medio =', medio)