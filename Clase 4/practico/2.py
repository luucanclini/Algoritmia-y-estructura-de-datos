N = abs(int(input('ingrese un entero para averiguar sus divisores y sumarlos todos: ')))
sumatoria = 0
print('divisores: ')
for i in range(1,N+1):
    if N%i == 0:
        print(i)
        sumatoria = sumatoria + i
print('la suma de los divisores da', sumatoria)
    