import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor('#ffbc4d')
turtle.title("Python Turtle")

turtle1 = turtle.Turtle()
'''
for i in range(5):
    turtle1.right(144)
    turtle1.forward(100)

turtle.done()
'''

num_sides = 6
angle = 360.0 / num_sides

for i in range(num_sides):
    turtle1.left(angle)
    turtle1.forward(100)

turtle.done()