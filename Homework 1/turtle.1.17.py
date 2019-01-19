import turtle
point1 = (-39, 48)
point2 = (50, -50)
turtle.pensize(5)
turtle.color("red")
turtle.penup()
turtle.goto(point1)
turtle.pendown()
turtle.write(str(point1))
turtle.goto(point2)
turtle.write(str(point2))
turtle.hideturtle()
turtle.exitonclick()

