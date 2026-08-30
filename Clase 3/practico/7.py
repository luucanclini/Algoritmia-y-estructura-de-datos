a=int(input('elija un valor para a: '))
digitos=int(input('cuantos digitos tiene a?: '))
d=int(input('que numero desea contar cuantas veces aparece?: '))
count = 0
aoriginal=a
for i in range(0,digitos):
    digito=a%10
    if digito==d:
        count = count + 1
    a=a//10
print('el numero',d,'aparece',count,'veces en',aoriginal)