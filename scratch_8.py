import turtle
n=turtle.Turtle()
n.speed(0)
color=['red','green','yellow','blue']
for i in range(200):
    n.color(color[i%4])
    n.fd(i)
    n.lt(90)



turtle.done()