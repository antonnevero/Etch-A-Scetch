from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
speed = 10



def forward():
    timmy.fd(10)

def back():
    timmy.bk(10)

def right():
    timmy.setheading(timmy.heading() - 10)
    timmy.fd(10)

def left():
    timmy.setheading(timmy.heading() + 10)
    timmy.fd(10)

def clear():
    timmy.reset()



screen.listen()
screen.onkeypress(fun=right, key="d")
screen.onkeypress(fun=left, key="a")
screen.onkeypress(fun=forward, key="w")
screen.onkeypress(fun=back, key="s")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
