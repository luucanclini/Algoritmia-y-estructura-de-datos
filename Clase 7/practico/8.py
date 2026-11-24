from math import exp, log


def pot(b, n):
    resultado = 1
    for _ in range(abs(n)):
        resultado = resultado * b
    if n < 0:
        return 1 / resultado
    return resultado


def pot_exp_log(b, n):
    if n == 0:
        return 1
    return exp(n * log(b))

print("8) 2^5 con for:", pot(2, 5))
print("8) 2^-3 con for:", pot(2, -3))
print("8) 5^0 con for:", pot(5, 0))
print("8) 2^5 con exp/log:", pot_exp_log(2, 5))