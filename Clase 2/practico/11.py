Vinicial = float(input('ingrese la velocidad inicial del ojeto arrojado al vacío: '))
Tinicial = float(input('ingrese el tiempo inicial: '))
Tfinal = float(input('ingrese el tiempo final: '))

if Tfinal<Tinicial:
    print('el tiempo final no puede ser menor al tiempo inicial')
elif Tinicial<0 or Vinicial<0:
    print('los valores deben ser positivos')
else: 
    Vfinal= Vinicial + 9.8 * (Tfinal-Tinicial)
    print("La velocidad final es: ", Vfinal)