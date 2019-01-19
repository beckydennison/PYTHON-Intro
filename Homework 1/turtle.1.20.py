import turtle


turtle.penup()
turtle.pencolor("black")
turtle.goto(-100, 50)
turtle.pendown()
turtle.pensize(5)

for _ in range (2):
    turtle.forward(200)
    turtle.right(135)
    turtle.forward(100)
    turtle.right(45)

turtle.right(90)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(135)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)

turtle.right(90)
turtle.forward(100)
turtle.left(135)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(180)
turtle.forward(100)
turtle.right(90)


for _ in range (2):
    turtle.forward(200)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(135)

turtle.hideturtle()
