from math import sin

print("Name:", __name__)

def inversa(s):
    resultado = ''
    for c in s:
        resultado = c + resultado
    return resultado

# ------ main --------------
if __name__  == "__main__":
    print("Soy la primera linea de ejemplo2")
    cadena = input("Ingrese cadena:")
    res = inversa(cadena)
    # Vemos que las variables son
    # inaccesibles desde el programa
    # principal
    # print(c, resultado, s)
    print("La inversa es ", res)
    print("Sin(8): ", sin(8))
    print("Name:", __name__)
