def es_palindromo(lista):
    if len(lista) == 0: return True
    elif len(lista) == 1: return True
    else:
        primero = lista[0]
        ultimo = lista[-1]
        if primero != ultimo: return False
        else:
            lista_sin_pri_ni_ult = lista[1:-1]
            # print(lista_sin_pri_ni_ult)
            return es_palindromo(lista_sin_pri_ni_ult)


print("pal(121): ", es_palindromo(list("121")))
print("pal(1): ", es_palindromo(list("1")))
print("pal(11): ", es_palindromo(list("11")))
print("pal(12344321): ", es_palindromo(list("12344321")))
print("pal(123454321): ", es_palindromo(list("123454321")))
print("pal(123): ", es_palindromo(list("123")))
           
           
