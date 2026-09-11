print('ingrese numeros para calcular su promedio, ingrese -1 cuando haya terminado')
num = 0
count = 1
max = -1
num = int(input('primer valor:'))
min = num
sumatoria = num

while True:
    count = count + 1
    num = int(input('siguiente valor:'))
    if num == -1:
        break
    if num>max:
        max = num
    if num<=min:
        min = num

    sumatoria = sumatoria + num
promedio = sumatoria / count

print('maximo:',max)
print('minimo:',min)
print('sumatoria:',sumatoria)
print('promedio:',promedio)