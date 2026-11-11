from ..LinkedBinaryTree import *

T1 = LinkedBinaryTree()

r1 = T1.add_root('*')

n2 = T1.add_left(r1,'+')
n3 = T1.add_right(r1,'-')

n4 = T1.add_left(n2,'/')
T1.add_right(n2,5)
T1.add_left(n3,5)
T1.add_right(n3,1)

T1.add_left(n4,18)
T1.add_right(n4,9)



T2 = LinkedBinaryTree()

r2 = T2.add_root('a')

nd = T2.add_left(r2,'d')
ne = T2.add_right(r2,'e')

nx = T2.add_left(nd,'x')
T2.add_right(nd,'z')
T2.add_left(ne,'b')
T2.add_right(ne,'k')

T2.add_left(nx,'f')



T3 = LinkedBinaryTree()

r3 = T3.add_root(3)

c2 = T3.add_left(r3,4)

c3 = T3.add_left(c2,8)
c4 = T3.add_right(c2,5)

c5 = T3.add_left(c3,1)
c6 = T3.add_left(c4,7)

c7 = T3.add_left(c5,6)
c8 = T3.add_right(c5,9)
c9 = T3.add_left(c6,3)

c10 = T3.add_left(c7,0)
c11 = T3.add_left(c8,3)