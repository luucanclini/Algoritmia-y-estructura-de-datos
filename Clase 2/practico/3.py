#3. Leer tres valores x, y, z y hallar el m ́ınimo entre ellos de 2 formas: (i) usando la funci ́on de librer ́ıa min varias veces y (ii) usando if-elif-else.
x = float(input('ingrese un valor para x: '))
y = float(input('ingrese un valor para y: '))
z = float(input('ingrese un valor para z: '))
m='el minimo es '
#i)
print(m,min(x,min(y,z)))
#ii)
if x<y and x<z:
    print(m,x)
elif y<z:
    print(m,y)
else:
    print(m,z)