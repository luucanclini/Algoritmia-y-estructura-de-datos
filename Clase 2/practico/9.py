print("vamos a calcular el volumen de una caja rectangular")
largo= float(input('ingrese el largo de la caja en cm:'))
altura= float(input('ingrese la altura de la caja cm:'))
fondo= float(input('ingrese el largo de la caja cm:'))
if largo==altura==fondo:
    print("estamos calculando el volumen de un cubo rectangular, no de un cubo")
elif largo<=0 or altura <=0 or fondo<=0:
    print("una caja debe tener medidas positivas")
else:
    volumen=altura*largo*fondo
    if volumen>1500:
        print('el volumen supera el metro y medio (',volumen,')')
    else:
        print('el volumen no supera el metro y medio (',volumen,')')