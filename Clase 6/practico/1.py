from math import sqrt

medidas = [34, 27, 45, 55, 22, 34]
list_size = len(medidas)
sumatoria = 0
sumatoria2 = 0

for i in range(list_size):
    sumatoria = sumatoria + medidas[i]

media = sumatoria / list_size
maximo = max(medidas)
minimo = min(medidas)

for i in range(list_size):
    sumatoria2 = sumatoria2 + (medidas[i] - media)**2

desvio = sqrt(sumatoria2/(list_size - 1))

print('media:',media)
print('maximo:',maximo)
print('minimo:',minimo)
print('desvio:',desvio)