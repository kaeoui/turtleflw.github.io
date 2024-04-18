import turtle

screen = turtle.Screen()
screen.bgcolor("orange")
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed(5)

def petalo(t, radio):
    t.pensize(1)
    t.pencolor("black")
    t.color("yellow")
    t.begin_fill()
    t.circle(radio, 60)
    t.left(120)
    t.circle(radio, 60)
    t.end_fill()
    t.pencolor("white")
    t.pensize(1)

def flor():
    radio = 100

    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.pensize(8)
    t.left(90)
    t.color("green")
    t.forward(180)

    for _ in range(10):
        petalo(t, radio)
        t.right(15)
        
##punto central de la flor
    t.penup()
    t.goto(1, 90)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

t.penup()
t.goto(-400, -100)
t.pendown()
t.color("black")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

##texto final
flor()
t.penup()
t.goto(0, -200)
t.speed(10)
t.color("white")
t.write("Eres la mejor novia del mundo, te amo mi amor. ", align="center", font=("Arial", 10, "bold"))

t.hideturtle()
turtle.done()