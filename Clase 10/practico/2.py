#funciones

def recibirNum():
    num = int(input('ingrese un valor para hallar sus primos anteriores:'))
    return num


def encontrarPrimos(tope):
    primos = []

    for valor in range(2,tope+1):
        esPrimo = True
        for i in range(2,valor):
            if valor%i == 0:
                esPrimo = False
        if esPrimo == True:
            primos.append(valor)
    return primos

def encontrarPrimosAtractivos(listaPrimos):
    primosAtractivos = []

    listaA= listaPrimos
    listaB= listaPrimos

    for a in listaA:
        for b in listaB:
            if a-b == 6:
                primosAtractivos.append((a,b))

    return primosAtractivos

#main
tope = recibirNum()
print('lista de primos atractivos en el rango de 0 y', tope,':',encontrarPrimosAtractivos(encontrarPrimos(tope)))