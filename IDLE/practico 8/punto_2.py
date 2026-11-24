inversa = []
def reverse(s):
    if s == []:
        return inversa
    else:
        inversa.insert(0,s[0])
        del s[0]
        return (reverse(s))

lista = [1,2,3,4,5]
print(reverse(lista))

def palindromo(s):
    esP = True
    if len(s)== 1 or len(s)==0:
        return esP
    else:
        if s[0] == s[-1]:
            del s[0]
            del s[-1]
            return palindromo(s)
        else:
            esP = False
            return esP
lista2 = [1,2,2,1]
print(palindromo(lista2))

lista3 = [9,5,3,8,7]

def minimo(s):
    if len(s)==1:
        return s[0]
    else:
        minim = s[0]
        del s[0]
        return min(minim,minimo(s))

numero = 43487

def maximo(n):
    if n < 10:
        return n
    else:
        maxim = n%10
        return max(maxim,maximo(n//10))

print('minimo de la lista: ',minimo(lista3))
print('maximo digito: ',maximo(numero))
