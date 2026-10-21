numeros = [1, '2', 3, 4, 5, 'seis', 8]
for nro in numeros:
   try:
      resultado = 10 / int(nro)
      print(resultado)
   except ValueError as e:
      print("Oops! No es un número válido.")
      print("Info: ", str(e))
   except ZeroDivisionError:
      print("Oops! No se puede dividir por cero.")
