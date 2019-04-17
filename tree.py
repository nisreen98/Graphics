import  turtle
t=turtle.Turtle()
t.pensize(3)
t.left(90)
t.fd(100)
t.left(30)
t.speed(600)
def drow(x):
    if(x<10):
        return
    else:
        t.pencolor('green')
        t.fd(x)
        t.left(30)
        drow(x*7/8)
        t.right(60)
        drow(x * 7 / 8)
        t.left(30)
        t.backward(x)
drow(50)
turtle.done()