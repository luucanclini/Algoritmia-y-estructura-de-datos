x=int(input('ingrese un valor para x: '))
print('los divisores de',x,'son:')
count=0
for i in range(1,x+1):
    if x%i==0:
        print(i)
        count=count+1

if count==2:
    print(x,'es un numero primo')
else:
    print(x,'no es primo')


