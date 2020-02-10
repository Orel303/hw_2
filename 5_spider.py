import turtle


def spider():
    turtle.shape("turtle")
    for i in range(12):
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)
        turtle.left(30)

if __name__=='__main__':
    spider()


