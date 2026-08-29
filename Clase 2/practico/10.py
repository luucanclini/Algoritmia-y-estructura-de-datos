altura = float(input('ingrese la altura desde la que se arrojo el objeto: '))
if altura<0.0:
    print('la altura no puede ser negativa')
else:
    velocidad = 2*9.8*altura
    print('la velocidad con la que el objeto impacta el piso es de:', velocidad)