N = int(input('ingrese un numero entero: '))
D = int(input('ingrese el digito que quiere averiguar si aparece en su numero entero: '))
aparece = False
while N>0 and not aparece:
    elemento = N%10
    if elemento == D:
        aparece = True
    else:
        N = N//10

if aparece:
    print('el digito', D,'si aparece')
else:
    print('el digito',D,'no aparece')