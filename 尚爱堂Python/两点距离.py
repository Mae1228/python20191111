import turtle
import math
import time
x1,y1=100,200
x2,y2=10,90
x3,y3=-62,20
x4,y4=-52,-60
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
d=math.sqrt((x1-x4)**2+(y1-y4)**2)
turtle.write(d)
turtle.done()
time1=time.time()
print(time1)
print(type(time1))