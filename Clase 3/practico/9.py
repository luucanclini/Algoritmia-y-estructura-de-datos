from math import comb
x=int(input('ingrese un valor para x: '))
y=int(input('ingrese un valor para y: '))
n=int(input('de que grado va a ser su binomio?: '))

binomio=(x+y)**n
sumatoria=0
for k in range(0,n+1):
    factor=comb(n,k)
    valor=(x**(n-k))*y**k
    sumatoria=sumatoria+(factor*valor)
print(binomio,'=',sumatoria)