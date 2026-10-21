''''
nro = int(input('ingrese un numero, devuelve falso si no es primo: '))
def primo(nro):
    esPrimo = True
    for i in range(2,nro):
        if nro%i == 0:
            esPrimo = False

    return esPrimo
print(primo(nro))
'''

''''
dia = int(input('ingrese el dia: '))
mes = int(input('ingrese el mes: '))
ano = int(input('ingrese el anio: '))

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def fecha_valida(dia,mes,ano):
    valido = True
    mensaje = 'fecha valida'
    mes31dias = (1,3,5,7,8,10,12)

    if dia<=0 or mes<=0 or ano<=0:
        valido = False
        mensaje = 'ninguna fecha puede ser negativa'

    if mes not in mes31dias and dia>30:
        valido = False
        mensaje = 'el mes elegido tiene hasta 30 dias'

    if es_bisiesto(ano) == False and mes==2 and dia==29:
        valido = False
        mensaje = 'el anio no es bisiesto, ingrese un dia valido'

    if mes == 2 and dia>29:
        valido = False
        mensaje = 'febrero tiene hasta 28 dias'

    if mes in mes31dias and dia>31:
        valido = False
        mensaje = 'los meses no tienen mas de 31 dias'

    if mes>12:
        valido = False
        mensaje = 'solo hay hasta 12 meses'

    return (valido,mensaje)

print (fecha_valida(dia,mes,ano))
'''

