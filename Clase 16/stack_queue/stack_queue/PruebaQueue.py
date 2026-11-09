from Empty import Empty
from ArrayQueue import *

Q = ArrayQueue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)

while not Q.is_empty():
    item = Q.dequeue()
    print(item)

    
