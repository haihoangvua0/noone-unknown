import turtle
v = turtle.Turtle()

#chuaanr bij
turtle.fillcolor ("blue")
turtle.begin_fill()

for i in range(4):
    v.forward(100)
    v.right(90)

v.left(60)
for i in range(3) :
    v.forward(100)
    v.right(120)

v.forward(100)
v.right(60)
v.forward(200)
v.right(60)
v.forward(100)
v.right(120)

for i in range(2):
    v.forward(200)
    v.lt(90)
    v.forward(100)
    v.left(90)
v.fd(300)
turtle.end_fill()


#laanf hai
turtle.Turtle().goto(-40.00, 220.00)
turtle.fillcolor ("red")
turtle.begin_fill()

#chayj mawtj troiwf

turtle.circle(50)
turtle.end_fill()


turtle.done()