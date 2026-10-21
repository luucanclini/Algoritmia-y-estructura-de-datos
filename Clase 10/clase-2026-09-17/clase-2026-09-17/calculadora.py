from restador import resta

SUMA     = "1"
RESTA    = "2"
PRODUCTO = "3"
SALIR    = "x"

def leer_numero(cartel):
    seguir = True
    while seguir:
        try:
            numero = float(input(cartel + " "))
            seguir = False
        except:
            print("Error: Ingrese nuevamente")
    return numero

def leer_operacion():
    print("Menu de operaciones")
    print("-------------------")
    print("1. suma")
    print("2. resta")
    print("3. producto")
    print("x. salir")
    seguir = True
    cantidad_intentos = 0
    while seguir:
        eleccion = input("Ingrese opcion: ")
        if len(eleccion) == 1 and \
           (eleccion >= "1" and eleccion <= "3") \
           or eleccion == "x":
            seguir = False
        else:
            print("Opcion incorrecta")
            cantidad_intentos += 1
            if cantidad_intentos == 4:
                raise Exception("Muchos errores! >:-(")
    return eleccion

def sumar(n1, n2):
    if type(n1) not in {float, int}:
        raise Exception("sumar: Primer argumento mal")
    # Deber: programar validar n2
    return n1 + n2

def mostrar_resultado(numero):
    mensaje = "El resultado es " + str(numero) + "."
    print(len(mensaje)*"-")
    print(mensaje)
    print(len(mensaje)*"-")
#-------------- Main --------------

operacion = leer_operacion()
nro1 = leer_numero("Ingrese numero 1:")
nro2 = leer_numero("Ingrese numero 2:")
if operacion == SUMA:
    resultado = sumar(nro1, nro2)
    mostrar_resultado(resultado)
elif operacion == RESTA:
    resultado = resta(nro1, nro2)
    mostrar_resultado(resultado)
elif operacion == PRODUCTO:
    # completar
    x=0
elif operacion == SALIR:
    # completar
    print("ADIOS")
