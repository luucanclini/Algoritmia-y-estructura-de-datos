n = int(input("Ingrese el valor máximo para buscar ternas: "))

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            if x**2 + y**2 == z**2:
                print(f"({x}, {y}, {z})")