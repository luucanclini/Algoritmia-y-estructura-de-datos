# factorial(n) = productoria de 
# i=1 a n de i.

def factorial(n):
    prod = 1
    for i in range(2,n+1):
        prod *= i
    return prod

print("fact(0): ", factorial(0))
print("fact(1): ", factorial(1))
print("fact(4): ", factorial(4))
print("fact(9): ", factorial(9))
print("fact(300): ", factorial(300))
