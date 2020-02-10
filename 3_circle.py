import turtle

def circle(r):
    turtle.shape("turtle")
    n = 360
    for i in range(n):
        turtle.forward(1)
        turtle.left(1)

    if __name__ == '__main__':
        circle(30)

