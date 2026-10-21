from math import sqrt

a = int(input('ingrese el valor para x^2: '))
b = int(input('ingrese el valor para x: '))
c = int(input('ingrese el valor para el termino independiente: '))

print('su polinomio =(',a,')x^2+(',b,')x+(',c,')')

def baskara(a,b,c):
    discriminante = (b**2)-4*a*c
    if discriminante<0:
        return None
    elif discriminante == 0:
        x1 = -b/(2*a)
        return(x1,x1)
    else:
        x1 = (-b-(sqrt(discriminante)))/2*a
        x2 = (-b+(sqrt(discriminante)))/2*a
        return(x1,x2)

print('raices del polinomio: ',baskara(a,b,c))