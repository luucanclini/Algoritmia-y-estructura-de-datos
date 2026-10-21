c = int(input('calcularemos el interes de un plazo fijo, ingrese su capital:'))
r = int(input('ingrese la taza de interes: '))
t = int(input('ingrese la cantidad de dias: '))

def plazo_fijo(c,r,t):
    numerador = c*t*r
    denominador = 36500
    i = numerador/denominador
    return i 
interes = plazo_fijo(c,r,t)
print('taza de interes: ',interes)
print('dinero total:', interes +c)