a=int(input('elija un valor para a: '))
digitos=int(input('cuantos digitos tiene a?: '))
count = 0
aoriginal=a
for i in range(0,digitos):
    digito=a%10
    if digito==3:
        count = count + 1
    a=a//10
print('el numero 3 aparece',count,'veces en',aoriginal)