import turtle
t=turtle.Pen()
t.width(4)
t.speed(0)
my_color=('red','blue','green','pink')
for i in range(30):#      0    1     2     3      4
    t.penup()
    t.goto(0,-i*10)#       0  -100  -200  -300 -400
    t.pendown()
    t.color(my_color[i%len(my_color)])
    t.circle(18+i*10)#   100   200   300   400  500







turtle.done()