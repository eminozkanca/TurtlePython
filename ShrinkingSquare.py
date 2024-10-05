import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("#ffbc4d")
turtle.title("Shrinking Squares")

turtle_emin = turtle.Turtle()
turtle_emin.color("blue")

def shrinkingsqaure(size):
    for i in range(20):
        turtle_emin.forward(size)
        turtle_emin.left(90)
        size = size - 10

shrinkingsqaure(180)
turtle.done()

