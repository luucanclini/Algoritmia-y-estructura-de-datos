# factorial(n) = de acuerdo
# a definicion recursiva

def factorial(n):
    if n==0: return 1
    else: return n * factorial(n-1)

print("fact(0): ", factorial(0))
print("fact(1): ", factorial(1))
print("fact(4): ", factorial(4))
print("fact(9): ", factorial(9))
print("fact(300): ", factorial(300))
