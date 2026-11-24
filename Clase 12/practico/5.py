
def insercion_ascendente(a):
    n = len(a)
    for i in range(1, n):
        actual = a[i]
        j = i - 1
        while j >= 0 and a[j] > actual:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = actual

def probar_ej5(tipo_dato, casos):
    print(f"\n=== EJERCICIO 5 - {tipo_dato} ===")
    for descripcion, arreglo in casos:
        copia = arreglo.copy()
        insercion_ascendente(copia)
        print(f"{descripcion}: {arreglo} -> {copia}")

casos_reales = [
    ("1. Vacío", []),
    ("2. Un elemento", [3.14]),
    ("3. Desordenado", [4.5, 1.2, 7.8, 3.0]),
    ("4. Todos distintos", [9.1, 2.4, 5.5, 1.0, 8.9]),
    ("5. Con repetidos", [4.2, 2.1, 4.2, 1.5, 2.1]),
    ("6. Todos iguales", [6.5, 6.5, 6.5, 6.5]),
    ("7. Ya ordenado ascendente", [1.1, 2.2, 3.3, 4.4]),
    ("8. Ya ordenado descendente", [4.4, 3.3, 2.2, 1.1])
]

casos_strings = [
    ("1. Vacío", []),
    ("2. Un elemento", ["python"]),
    ("3. Desordenado", ["perro", "arbol", "zorro", "casa"]),
    ("4. Todos distintos", ["uva", "banana", "manzana", "kiwi"]),
    ("5. Con repetidos", ["sol", "luna", "sol", "estrella", "luna"]),
    ("6. Todos iguales", ["dato", "dato", "dato"]),
    ("7. Ya ordenado ascendente", ["a", "b", "c", "d"]),
    ("8. Ya ordenado descendente", ["d", "c", "b", "a"])
]

probar_ej5("Números Reales", casos_reales)
probar_ej5("Cadenas de Caracteres", casos_strings)