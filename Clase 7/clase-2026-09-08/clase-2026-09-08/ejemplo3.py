from ejemplo2 import inversa

def imprimir_n_veces(s, n):
    for _ in range(n):
        print(s)

print("Soy la primera linea de ejemplo3")
otra_cadena = "1234"
una_cadena = inversa(otra_cadena)
print( "una cadena: ", una_cadena )
imprimir_n_veces( "pepe", 8 )
print("Chau")
# Lo siguiente es una mala practica:
valor =  imprimir_n_veces("a", 3)
print("valor: ", valor)
# valor vale None porque la funcion no devolvio nada.

