n = int(input('ingrese un valor para descomponerlo en sus factores primos: '))
lista_primos = []

for numero in range(2, n + 1):
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        lista_primos.append(numero)
print(lista_primos)



for primo in lista_primos:
    while n%primo == 0:
        factor = n
        n = n/primo
        print(factor,'|',primo)
print(1)