def cantFilas(a):
    return len(a)
def cantColumnas(a):
    return len(a[0])


def esMatrizSimetrica(a):

    for i in range(cantFilas(a)):
        for j in range(cantColumnas(a)):
            if a[i][j] != a[j][i]:
                return False
    
    return True