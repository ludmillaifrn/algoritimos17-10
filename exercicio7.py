import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(90)

turtle.backward(50)
turtle.backward(200)
turtle.right(90)

for _ in range(3):
  turtle.forward(90)
  turtle.left(90)