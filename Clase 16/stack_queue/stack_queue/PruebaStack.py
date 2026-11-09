from Empty import Empty
from ArrayStack import *

S = ArrayStack() # contents: [ ]
S.push(5) # contents: [5]
S.push(3) # contents: [5, 3]
print(len(S)) # contents: [5, 3]; outputs 2
print(S.pop()) # contents: [5]; outputs 3
print(S.is_empty( )) # contents: [5]; outputs False
print(S.pop( )) # contents: [ ]; outputs 5
print(S.is_empty( )) # contents: [ ]; outputs True
S.push(7) # contents: [7]
S.push(9) # contents: [7, 9]
print(S.top()) # contents: [7, 9]; outputs 9
S.push(4) # contents: [7, 9, 4]
print(len(S)) # contents: [7, 9, 4]; outputs 3
print(S.pop()) # contents: [7, 9]; outputs 4
S.push(6) # contents: [7, 9, 6]
