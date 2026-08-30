n = int(input('cuantos numeros desea ingresar?: '))
a = int(input('ingrese el primer valor: '))
sumaTotal=a
minimo=a
maximo=a
for i in range(1,n):
    b=int(input('ingrese el siguiente valor: '))
    minimo=min(minimo,min(a,b))
    maximo=max(maximo,max(a,b))
    sumaTotal=sumaTotal+b
print('maximo: ',maximo,', minimo: ',minimo,', suma: ',sumaTotal)