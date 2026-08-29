#5. Resolver la ecuaci ́on cuadr ́atica ax2+bx+c = 0 usando el algoritmo de Bazkara pero: (i) determinar
#que a no es cero (cuando lo es indicar que la ecuaci ́on no es cuadr ́atica), identificar cu ́ando hay 0,
#1, o 2 soluciones discriminando los casos e imprimiendo las soluciones.
from math import isclose, sqrt
a= float(input('ingrese un valor para a:'))
b= float(input('ingrese un valor para b:'))
c= float(input('ingrese un valor para c:'))

discriminante= b**2-4*a*c
if isclose(a,0.0):
    print('el polinomio debe tener el coeficiente a distinto de 0')
else:
    if abs(discriminante)==0:
        x = -b/(2*a)
        print("el polinomio tiene una sola raiz, x =",x)
    elif discriminante>0:
        raiz = sqrt(discriminante)
        x1 = (-b+raiz)/(2*a)
        x2 = (-b-raiz)/(2*a)
        print("el polinomio tiene dos raices, x1 =",x1, 'y x2 =',x2)
    else:
        print("el polinomio no tiene raices reales")    