a = 23
b = 0
c = "A"
try:
    resultado = a/b
except ZeroDivisionError:
    print("Error, division por cero.")
except TypeError:
    print("Error en el tipo de dato.")

# Resultado:  Error, division por cero.
try:
    resultado = a/c
except ZeroDivisionError:
    print("Error, division por cero.")
except TypeError:
    print("Error en el tipo de dato.")
# Resultado: Error en el tipo de dato

print("---------------------------")
import sys
try:
    resultado = a / c
except:
    print("Info del error: ", sys.exc_info()) 
