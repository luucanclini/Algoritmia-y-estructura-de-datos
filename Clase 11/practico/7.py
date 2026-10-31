def diagonalPrincipal(a):
    diagonal = (a[0][0] * a[1][1] * a[2][2]) + (a[0][1] * a[1][2] * a[2][0]) + (a[0][2] * a[1][0] * a[2][1])
    return diagonal

def diagonalSecundaria(a):
    diagonal = (a[0][2] * a[1][1] * a[2][0]) + (a[0][0] * a[1][2] * a[2][1]) + (a[0][1] * a[1][0] * a[2][2])
    return diagonal

def det3(a):
    determinante = diagonalPrincipal(a)-diagonalSecundaria(a)
    return determinante