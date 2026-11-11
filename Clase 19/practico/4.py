def grado(A):
    maximo = 0

    for n in A.positions():
        maximo = max(maximo,len(A.children(n)))

    print('grado:', maximo)