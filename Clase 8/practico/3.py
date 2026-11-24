def reverse(s):
    if len(s) == 0:
        return []
    else:
        return reverse(s[1:]) + [s[0]]

def es_palindromo(s):
    if len(s) <= 1:
        return True
    else:
        return (s[0] == s[-1]) and es_palindromo(s[1:-1])

def minimo_lista(s):
    if len(s) == 1:
        return s[0]
    else:
        min_resto = minimo_lista(s[1:])
        if s[0] < min_resto:
            return s[0]
        else:
            return min_resto

def max_digito(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        ultimo = n % 10
        max_resto = max_digito(n // 10)
        if ultimo > max_resto:
            return ultimo
        else:
            return max_resto

# Prueba 3a
print("3a) Inversa de [1, 2, 3, 4]:", reverse([1, 2, 3, 4]))
print("3a) Inversa de []:", reverse([]))

# Prueba 3b
print("3b) 'neuquen' es palíndromo?:", es_palindromo("neuquen"))
print("3b) 'python' es palíndromo?:", es_palindromo("python"))

# Prueba 3c
print("3c) Mínimo de [8, 3, 15, 2, 9]:", minimo_lista([8, 3, 15, 2, 9]))

# Prueba 3d
print("3d) Máximo dígito de 48291:", max_digito(48291))
print("3d) Máximo dígito de 7:", max_digito(7))