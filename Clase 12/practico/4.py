def seleccion_decreciente(a):
    n = len(a)
    for i in range(n - 1):
        pos_max = i
        for j in range(i + 1, n):
            if a[j] > a[pos_max]:
                pos_max = j
        a[i], a[pos_max] = a[pos_max], a[i]

def probar_casos(nombre_prueba, casos):
    print(f"=== {nombre_prueba} ===")
    for descripcion, arreglo in casos:
        copia = arreglo.copy()
        seleccion_decreciente(copia)
        print(f"{descripcion}: {arreglo} -> {copia}")

casos_enteros = [
    ("1. Vacío", []),
    ("2. Un elemento", [5]),
    ("3. Desordenado", [4, 1, 7, 3]),
    ("4. Todos distintos", [9, 2, 5, 1, 8]),
    ("5. Con repetidos", [4, 2, 4, 1, 2]),
    ("6. Todos iguales", [7, 7, 7, 7]),
    ("7. Ya ordenado ascendente", [1, 2, 3, 4, 5]),
    ("8. Ya ordenado descendente", [5, 4, 3, 2, 1])
]

probar_casos("EJERCICIO 4 - Decreciente (Enteros)", casos_enteros)