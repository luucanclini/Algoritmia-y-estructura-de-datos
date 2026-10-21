def pot(a,n):
    if n==0: return 1
    else: return a * pot(a,n-1)

def cd(n):
    if n>=0 and n<=9: return 1
    else: return 1 + cd(n // 10)

print("2^10: ", pot(2, 10))
print("cantidad de digitos de 12345678765:", cd(12345678765))
