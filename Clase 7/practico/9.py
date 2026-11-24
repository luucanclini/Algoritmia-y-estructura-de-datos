def fact(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact(n) // (fact(k) * fact(n - k))

print("9) 5! =", fact(5))
print("9) 0! =", fact(0))
print("9) Combinatorio (5 tomados de a 2):", comb(5, 2))