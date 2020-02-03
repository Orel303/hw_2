import turtle

def rectangle(k):
    for _ in range(4):
        turtle.forward(k)
        turtle.left(90)


if __name__=='__main__':
    rectangle(200)