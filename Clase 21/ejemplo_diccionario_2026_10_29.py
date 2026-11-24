d1 = { "Sergio" : 100, "Martin" : 8, \
       "Matias" : 7 }

print("d1: ", d1)
print("Tipo de d1: ", type(d1))

lista = [("Sergio", 100), ("Martin",8),\
            ("Matias", 7)]
d2 = dict( lista )
print("d2: ", d2)

print("valor de Martin: ", d1["Martin"])

try:
    print("Busco una clave inexistente.")
    print("valor de Tito: ", d1["Tito"])
except KeyError as e:
    print( "No esta: ", str(e) )

print("Le cambio el valor a Sergio por 80:")
d1["Sergio"] = 80
print("valor de Sergio: ", d1["Sergio"])
print("Eliminar (delete) a Sergio: ")
del d1["Sergio"]
try:
    print("Busco una clave inexistente.")
    print("valor de Sergio: ", d1["Sergio"])
except KeyError as e:
    print( "No esta: ", str(e) )

try:
    print("Trato de eliminar clave inexistente:")
    del d1["Valentino"]
except KeyError:
    print("No pude borrarlo")

print("d1: ", d1)
if "Tobias" in d1:
    print("Tobias esta")
else:
    print("Tobias no esta")

print("Claves de d1: ", d1.keys())
for k in d1.keys():
    print("k: ", k)
print("Valores de d1: ", d1.values())
for v in d1.values():
    print("v: ", v)
print("Entradas de d1: ", d1.items())
for e in d1.items():
    # (k,v) = e
    # k = e[0]; v=e[1]
    k, v = e
    print("k: ", k, "v: ", v)
print("Cantidad de entradas: ", d1.__len__())
print("Cantidad de entradas: ", len(d1))

valor_tito = d1.get("Tito")
if valor_tito is None:
    print("Tito no esta")
else:
    print('El valor de Tito: ', valor_tito)
















