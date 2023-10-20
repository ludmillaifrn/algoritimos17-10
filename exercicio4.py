import turtle
import random

turtle = turtle.Turtle()
colors = ['aquamarine','funchsia', 'blue','bisque','orange']

for _ in [1, 2, 3,]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(200)
    turtle.left(120)