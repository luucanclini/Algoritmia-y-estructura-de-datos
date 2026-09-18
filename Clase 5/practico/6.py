colores = ('azul','rojo','amarillo','verde','naranja')
print('seleccione que opcion quiere\n1)azul\n2)rojo\n3)amarillo\n4)verde\n5)naranja')
opcion=0

while opcion<1 or opcion>5:
    opcion = int(input('opcion: '))
    if opcion<1 or opcion>5:
        print('ups, opcion incorrecta, elija de nuevo...')
opcion -= 1
print('eligio el color',colores[opcion])
