#4. Hallar el m ́ınimo entre x e y pero esta vez notar cuando son iguales e indicando la identidad de m ́ınimo adem ́as de su valor.
x = float(input('ingrese un valor para x: '))
y = float(input('ingrese un valor para y: '))
m='el minimo es '

if x<y:
    print(m,'x=',x)
elif x>y:
    print(m,'y=',y)
else:
    print("son iguales ya que x =",x,'= y')