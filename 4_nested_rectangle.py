import turtle
from rectangle import rectangle

def nested_rectangle(n):
    for i in range(1, n):
        rectangle(10 + 10* i)
        turtle.penup()
        turtle.goto(-5*i, -5*i)
        turtle.pendown()


if __name__=='__main__':
    nested_rectangle(10)