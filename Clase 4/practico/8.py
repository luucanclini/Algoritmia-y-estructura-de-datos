from math import tan
print('tabla de valores para f (x) = 3 tan(x), para x ∈[1, 10]')

x = 1.0

while x <= 10:
    fx = 3*(tan(x))
    print('f(',x,') =',fx)
    x = x + 0.2