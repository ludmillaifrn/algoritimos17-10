import turtle

turtle = turtle.Turtle()
turtle.shape('square')
turtle.pensize(5)

for color in ['pink', 'black', 'pink', 'black']:
    turtle.color(color)
    turtle.forward(90)
    turtle.right(90)
turtle.penup()
turtle.right(10)
turtle.forward(200)
turtle.pendown()
for color in ['pink', 'black', 'pink', 'black']:
    turtle.color(color)
    turtle.forward(90)
    turtle.right(90)