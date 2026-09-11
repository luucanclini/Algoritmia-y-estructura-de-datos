n=int(input("ingrese un numero entero: "))
d=int(input("ingrese que digito quiere contar cuantas veces aparece en el nuemro entero: "))
a=n
nuevoValor=0
count = 0
while n>0:
    nuevoValor = n%10
    if nuevoValor == d:
        count=count+1
    n = n//10

print(d,"aparecio",count, 'veces en',a,)
