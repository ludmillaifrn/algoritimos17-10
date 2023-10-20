import turtle
import random

turtle = turtle.Turtle()
colors = ['cyan', 'blue', 'yellow', 'green', 'pink', 'purple', 'red','orange']

for c in range(180):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(2)
    turtle.right(2)
    
   