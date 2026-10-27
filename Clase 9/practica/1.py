from math import sin,sqrt
def f(x,y,z):
    factor1 = 1/(x-5)
    factor2=2/(2*x+5*y)
    factor3=3/((sin(3*z)**2))
    factor4= sqrt(x+y+z)
    resultado= factor1+factor2+factor3-factor4
    return resultado

print('ingrese valores para x,y,z:')
x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))
try:
    print('resultado:',f(x,y,z))
except ZeroDivisionError:
    print("no se puede dividir por 0, intente de nuevo")
except ValueError as e:
        print("error", e)