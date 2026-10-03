import turtle

t =turtle.Turtle()



def square(x, y, l):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+l, y)
    t.goto(x+l, y+l)
    t.goto(x, y+l)
    t.goto(x,y)

    if l > 10:
        square(x+l*3/4, y+l/4, l/2)
        square(x-l*1/4, y+l/4, l/2)
        square(x+l*1/4, y-l/4, l/2)



#square(-100,-100,200)


def branch(sz, level):

  if level > 0:
    t.forward(sz)
    t.right(30)
    branch(0.8*sz, level -1)
    t.right(-60)
    branch(0.8*sz, level -1)
    t.right(30)
    t.forward(-sz)

t.setheading(90)

branch(70,7)

turtle.mainloop()