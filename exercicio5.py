import turtle

turtle = turtle.Turtle()
turtle.color('red')

turtle.shape('circle')
for _ in [1, 2, 3]:
    turtle.forward(150)
    turtle.right(120)
    turtle.color('blue')

turtle.shape('turtle')
for _ in [1, 2, 3, 4]:
  turtle.forward(150)
  turtle.right(90)
  turtle.color('pink')