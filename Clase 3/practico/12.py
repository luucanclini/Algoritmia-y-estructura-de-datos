n = int(input("ingrese la cantidad de numeros q va a usar: "))
max1 = -0.01
max2 = -0.01
for i in range(n):
    x = int(input("valor de x: "))
    if x>=max1:
        max2=max1
        max1=x
    elif x<max1:
        max2=x

print("el numero mas grande es:", max1)
print("el segundo numero mas grande es:", max2)