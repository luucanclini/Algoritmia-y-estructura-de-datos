print("Arranco aca")
try:
    print("Hola")
    y = 7 / (1-1)
    # x = 8 # si esta eso => no hay except
    print(x)
    print("chau")
except NameError:
    print("Hay una variable sin definir")
except:
    print("Paso algo malo y no se que es")
    print("Me despido")
finally:
    print("Siempre me ire a mi casa")

print("Aca van comandos como siempre")
