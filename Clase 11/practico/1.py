from math import sqrt

def norma(vector):
    sumatoria = 0
    for elemento in vector:
        sumatoria = (elemento**2) + sumatoria

    return sqrt(sumatoria)

print(norma([2,3]))