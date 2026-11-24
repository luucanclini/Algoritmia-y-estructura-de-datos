
def leer_archivo_numeros(archivo):
    numeros = []
    try:
        with open(archivo, 'r') as file:
            for linea in file:
                numero = int(linea.strip())
                numeros.append(numero)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")
    except ValueError:
        print(f"Error al leer el archivo '{archivo}': No todos los datos son números enteros válidos.")
    return numeros

def es_maduro(n):
    if n <= 0:
        return False
    posicion = 1
    while n > 0:
        digito = n % 10
        if (posicion % 2) != (digito % 2):
            return False
        n = n // 10
        posicion += 1
    return True

def armar_lista_d(A, B, C):
    D = []
    for num in A:
        if es_maduro(num) and (num not in B) and (num not in C):
            D.append(num)
    
    if len(A) > 0:
        D.append(max(A))
    if len(B) > 0:
        D.append(max(B))
    if len(C) > 0:
        D.append(max(C))
        
    return D

def main():
    A = leer_archivo_numeros("a.txt")
    B = leer_archivo_numeros("b.txt")
    C = leer_archivo_numeros("c.txt")
    
    D = armar_lista_d(A, B, C)
    
    print("Lista A:", A)
    print("Lista B:", B)
    print("Lista C:", C)
    print("Lista D:", D)

main()