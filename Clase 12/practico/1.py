def buscar_lineal(a,n,y):
    for i in range(n):
        #print(i)
        if y == a[i][1]:
            return i
    return -1