import turtle
t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

#triagle
angle1 = 120
for i in range(3):
    t.fd(100)
    t.lt(angle1)

t.penup()
t.left(60)
t.fd(100)
t.rt(30)
t.pd()
t.fd(200)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(200)
t.pu()
t.back(200)
t.lt(60)
t.pd()
t.fd(100)
t.rt(60)
t.fd(200)
t.pu()
t.goto(-50,300)
t.pendown()

t.fillcolor("red")
t.begin_fill()
t.circle(100)
t.end_fill()

turtle.done()
