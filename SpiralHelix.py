import random
import turtle

turtle_screen = turtle.Screen()
turtle.bgcolor("yellow")
turtle.title("Turtle Spiral Helix")

turtleE = turtle.Turtle()
turtleE.color("blue")

turtle_colors = ["blue", "orange", "green", "purple", "red"]

for i in range(20):
    turtleE.speed(0)
    turtleE.color(turtle_colors[i % 5])
    turtle.circle(10 * i)
    turtle.circle(-10 * i)
    turtle.left(i)

turtle.done()