A = float(input('ingrese la altura de la persona en metros: '))
m='la persona es'
if A<=0.4:
    print('una persona no puede medir',A,'metros')
else:
    if A<1.50:
        print(m,'pequeña')
    elif 1.50<=A<1.80:
        print(m,'regular')
    elif 1.80<=A<2.10:
        print(m,'alta')
    else:
        print(m,'gigante')