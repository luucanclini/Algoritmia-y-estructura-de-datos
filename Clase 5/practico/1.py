cadena = input("ingrese una cadena: ")
largo = len(cadena)
count = 0
sumatoria = 0

for c in cadena:
    if '0' <= c <= '9':
        valor = float(c)
        count = count + 1
        sumatoria = sumatoria + valor

if count == largo:
    print('la cadena solo tiene digitos, su sumatoria es:',sumatoria)
elif count == 0:
    print('la cadena no tiene ningun digito')
else:
    print('la cadena no tiene solo digitos, la suma de los digitos es:',sumatoria)

