a = int(input('ingrese una valor para a: '))
b = int(input('ingrese una valor para b: '))
contador=0
for i in range(a,b+1):
    if i%5==0:
        contador = contador+1
print('entre',a,'y',b,'hay',contador,'multiplos de 5')