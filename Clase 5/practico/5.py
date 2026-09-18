palabra = input('ingrese una palabra: ').lower()
largo = len(palabra)
nuevaPalabra=''
for i in range(0,largo):
    if i%2 == 0:
        nuevaPalabra = nuevaPalabra + palabra[i].upper()
    else:
        nuevaPalabra = nuevaPalabra + palabra[i].lower()
print(nuevaPalabra)