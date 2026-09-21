# Error xq superficie_rectangulo no esta definido
# todavia.
# x = superficie_rectangulo(9)

def superficie_rectangulo(base, altura=7):
    return base * altura

sup1 = superficie_rectangulo( 3, 2 )
print("sup1: ", sup1)

sup2 = superficie_rectangulo( base=3, altura=2 )
print("sup2: ", sup2)

sup3 = superficie_rectangulo( altura=2, base=3 )
print("sup3: ", sup3)

# Solo especifico la base como 8
# y la altura vale por defecto 7
sup4 = superficie_rectangulo( 8 )
print("sup4: ", sup4)

