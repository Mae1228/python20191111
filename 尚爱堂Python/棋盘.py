import turtle
x=int(input('请输入边长'))
t=turtle.Pen()
# t.goto(0,100)
t.speed(10)
for i in range(x*2//50+1):
    t.penup()
    t.goto(-x,x-i*50)
    t.pendown()
    t.goto(x,x-i*50)
for i in range(x*2//50+1):
    t.penup()
    t.goto(-x + i * 50,x)
    t.pendown()
    t.goto(-x+i*50,-x)
# t.penup()
# t.goto(-300,280)
# t.pendown()
# t.goto(300,280)





turtle.done()