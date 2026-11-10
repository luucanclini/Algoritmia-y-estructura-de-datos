from ..arbol.arbol.LinkedTree import *

T1 = LinkedTree()

r1 = T1.add_root(1)

n2 = T1.add_last_child(r1,2)
n3 = T1.add_last_child(r1,3)

n4 = T1.add_last_child(n2,4)
n5 = T1.add_last_child(n2,5)
n6 = T1.add_last_child(n3,6)
n7 = T1.add_last_child(n3,7)

T1.add_last_child(n4,8)
T1.add_last_child(n4,9)
T1.add_last_child(n5,10)
n11 = T1.add_last_child(n6,11)
n12 = T1.add_last_child(n7,12)

T1.add_last_child(n11,13)
n14 = T1.add_last_child(n12,14)

T1.add_last_child(n14,15)



T2 = LinkedTree()

r2 = T2.add_root('a')

e2 = T2.add_last_child(r2,'d')
e3 = T2.add_last_child(r2,'v')
e4 = T2.add_last_child(r2,'e')

e5 = T2.add_last_child(e2,'x')
e6 = T2.add_last_child(e2,'y')
e7 = T2.add_last_child(e2,'z')
e8 = T2.add_last_child(e3,'u')
T2.add_last_child(e4,'b')
T2.add_last_child(e4,'k')

T2.add_last_child(e5,'f')
T2.add_last_child(e6,'n')
e13 = T2.add_last_child(e8,'t')

e14 = T2.add_last_child(e13,'h')

T2.add_last_child(e14,'p')



T3 = LinkedTree()

r3 = T3.add_root(3)

a2 = T3.add_last_child(r3,4)

a3 = T3.add_last_child(a2,8)
a4 = T3.add_last_child(a2,9)
a5 = T3.add_last_child(a2,5)

a6 = T3.add_last_child(a3,1)
T3.add_last_child(a4,4)
a8 = T3.add_last_child(a5,7)

a9 = T3.add_last_child(a6,6)
a10 = T3.add_last_child(a6,9)
T3.add_last_child(a8,3)

T3.add_last_child(a9,0)
T3.add_last_child(a10,3)