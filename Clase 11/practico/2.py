def prueba(a,b):
    if len(a)!=len(b):
        raise ValueError('los vectores deben ser de la misma dimension')
    
def productoEscalar(v,w):

    prueba(v,w)
    sumatoria = 0

    for i in range(len(v)):
        sumatoria = (v[i]*w[i]) + sumatoria

    return sumatoria
a=[2,3]
b=[4,5,0]

print(productoEscalar(a,b))