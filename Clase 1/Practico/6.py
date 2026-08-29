from math import pi
print('Para calcular la superficie y el volumen de una esfera porfavor ingrese')
radio = float(input('el radio:'))

superficie = 4*pi*(radio**2)
numerador = 4*pi*(radio**3)
volumen = numerador/3
print('la superficie es de ', superficie,'y el volumen es de', volumen)