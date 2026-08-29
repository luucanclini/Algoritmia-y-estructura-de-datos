#2. Leer dos valores x e y y hallar el m ́ınimo entre ellos de dos formas: (i) usando la funci ́on de librer ́ıa min y (ii) haciendo un if-else.
x = float(input('ingrese un valor para x: '))
y = float(input('ingrese un valor para y: '))
m='el minimo es '
#i)
print(m,min(x,y))
#ii)
if x<y:
    print(m,x)
else:
    print(m,y)