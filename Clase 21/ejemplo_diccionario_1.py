d1 = { 'Sergio' : 100, 'Martin' : 8, 'Matias' : 7 }
print("d1: ", d1)

conj_pares = {('Sergio', 100), ('Martin',8), ('Matias',7)}
print("Conjunto pares: ", conj_pares)

print("Tipo de d1: ", type(d1))
print("Tipo de conj pres: ", type(conj_pares))

if type(d1) is dict: print("Si, d1 es un dicionario")
else: print("d1 no es un diccionario")

if type(d1) is set: print("Si, d1 es un conjunto")
else: print("d1 no es un conjunto")

# Creo un dict d2 a partir del set de pares:
d2 = dict(conj_pares)
print("d2: ", d2)

print("Testeo de pertenencia y recuperacion: ")
clave = input("Ingrese clave: ")
if clave in d1:
    print("Esta y el valor asociado es: ", d1[clave])
else:
    print("Esa clave no esta en d1")
print("Agrego clave nueva:")
d1["Juan"] = 1000
d1["Tito"] = 80
d2["Maria"] = 99
try:
    print("d1 de Juan: ", d1['Juan'], " Espero 1000")
    print("d1 de Esteban: ", d1['Esteban'])
except KeyError as e:
    print("Fallo el diccionario con: ", str(e))

print("Elimino a Juan del diccionario: ")
del d1["Juan"]
print( "Esta Juan ahora en d1?: ", "Juan" in d1 )

print("Claves de d1: ", d1.keys())
print("Valores de d1: ", d1.values())
print("Entradas de d1: ", d1.items())
print("Tamano de d1: ", len(d1))
print("Imprimo clave de d1: ")
for clave in d1.keys():
    print(clave)
print("Testeo de clave no existente (devuelve None):")
print(d1.get("XXXXXXX"))
print("Testeo de clave existente:")
print(d1.get("Martin"))
