def mcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def simplificar(num, den):
    if den < 0:
        num = -num
        den = -den
    divisor = mcd(num, den)
    return (num // divisor, den // divisor)

def producto(f1, f2):
    a, b = f1
    c, d = f2
    if b == 0 or d == 0:
        raise ValueError("El denominador de una fracción no puede ser cero.")
    return simplificar(a * c, b * d)

def inversa(f):
    a, b = f
    if b == 0:
        raise ValueError("La fracción original tiene denominador cero.")
    if a == 0:
        raise ValueError("No existe la inversa de cero (quedaría denominador cero).")
    return simplificar(b, a)

# --- Programa de prueba ---
try:
    print("Producto (2/3) * (9/4):", producto((2, 3), (9, 4)))       # (3, 2)
    print("Producto (-1/2) * (4/5):", producto((-1, 2), (4, 5)))     # (-2, 5)
    print("Inversa de (3/4):", inversa((3, 4)))                      # (4, 3)
    print("Inversa de (-2/5):", inversa((-2, 5)))                    # (-5, 2)
except ValueError as error:
    print("Error:", error)

# Casos de prueba que lanzan excepción
try:
    print("Producto con denominador 0:", producto((1, 0), (2, 3)))
except ValueError as error:
    print("Error esperado en producto:", error)

try:
    print("Inversa de fracción nula (0/5):", inversa((0, 5)))
except ValueError as error:
    print("Error esperado en inversa:", error)