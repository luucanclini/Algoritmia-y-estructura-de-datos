from ..LinkedBinaryTree import *
exp = []
def postorden(A,v):
    if A.has_left(v):
        postorden(A,A.left(v))
    if A.has_right(v):
        postorden(A,A.right(v)) 

    exp.append(v.element())
    return exp

def pasarAString(exp):
    string = ''
    for c in exp:
        c = str(c)
        string = string + c + ' '
    return string