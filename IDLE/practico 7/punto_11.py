def integral(f,a,b,n):
    termino1 = (b-a)/n
    subtermino1=(f(a)+f(b))/2
    sumatoria = 0
    for k in range(1,n):
        valor = a + (k*((b-a)/n))
        sumatoria = sumatoria + f(valor)

    resultado = termino1*(subtermino1 + sumatoria)
    return resultado
