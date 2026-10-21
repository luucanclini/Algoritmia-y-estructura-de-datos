def primo(nro):
    if nro <= 1:
        return False
        
    for i in range(2, nro):
        if nro % i == 0:
            return False
            
    return True

nro = int(input('ingrese un numero, devuelve falso si no es primo: '))
print(primo(nro))