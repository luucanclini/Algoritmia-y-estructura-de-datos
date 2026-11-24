def invertir_con_lista(num):
    cadena = str(num)          
    lista = list(cadena)       
    lista.reverse()           
    cadena_inv = "".join(lista) 
    return int(cadena_inv)    

print("7) Invertir 12345:", invertir_con_lista(12345))
print("7) Invertir 490:", invertir_con_lista(490))