from math import cos
a = [x for x in range(111) if x%3==0]
b = [x for x in range(0,1000) if x%21 == 0]
c = {x for x in range(10,20000) if x%18 == 0 or x%27 == 0}
d = [x**3 for x in range(10,51) if cos(x)<0.5]