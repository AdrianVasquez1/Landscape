import turtle

scn = turtle.Screen()
bob = turtle.Turtle()
joe = turtle.Turtle()
jim = turtle.Turtle()
sue = turtle.Turtle()
tom = turtle.Turtle()
bill = turtle.Turtle()

bill.speed(10)
bob.speed(10)
sue.speed(10)
joe.speed(10)
jim.speed(10)

bill.penup()
bill.goto(-360, 335)
bill.pendown()
bill.color("light sky blue")
bill.begin_fill()
bill.forward(720)
bill.right(90)
bill.forward(670)
bill.right(90)
bill.forward(720)
bill.right(90)
bill.forward(670)
bill.end_fill()



sue.penup()
sue.goto(-357, -200)
sue.color("forest green")
sue.pendown()
sue.begin_fill()
sue.forward(710)
sue.right(90)
sue.forward(135)
sue.right(90)
sue.forward(710)
sue.right(90)
sue.forward(135)
sue.end_fill()

bob.penup()
bob.goto(-357,-200)
bob.color("red")
bob.pendown()
bob.begin_fill()
bob.left(90)
bob.forward(200)
bob.right(90)
bob.forward(200)
bob.right(90)
bob.forward(200)
bob.right(90)
bob.forward(200)
bob.end_fill()

jim.penup()
jim.goto(-359, 0)
jim.pendown()
jim.begin_fill()
jim.left(45)
jim.forward(145)
jim.right(90)
jim.forward(143)
jim.end_fill()
jim.penup()
jim.goto(-285,-200)
jim.begin_fill()
jim.color("saddle brown")
jim.left(135)
jim.pendown()
jim.forward(75)
jim.right(90)
jim.forward(60)
jim.right(90)
jim.forward(75)
jim.end_fill()

joe.penup()
joe.goto(250, -200)
joe.color("saddle brown")
joe.pendown()
joe.begin_fill()
joe.left(90)
joe.forward(200)
joe.right(90)
joe.forward(40)
joe.right(90)
joe.forward(200)
joe.end_fill()
joe.penup()
joe.color("dark green")
joe.goto(175, 0)
joe.pendown()
joe.begin_fill()
joe.circle(100)
joe.end_fill()

tom.penup()
tom.goto(50, -175)
tom.color("Orange Red")
tom.begin_fill()
tom.pendown()
tom.forward(100)
tom.left(90)
tom.forward(50)
tom.left(90)
tom.forward(50)
tom.right(45)
tom.forward(50)
tom.left(45)
tom.forward(100)
tom.left(45)
tom.forward(50)
tom.right(45)
tom.forward(50)
tom.left(90)
tom.forward(50)
tom.left(90)
tom.forward(200)
tom.end_fill()
tom.penup()
tom.color("yellow")
tom.goto(-120, -125)
tom.pendown()
tom.begin_fill()
tom.forward(15)
tom.right(90)
tom.forward(15)
tom.right(90)
tom.forward(15)
tom.right(90)
tom.forward(15)
tom.end_fill()
tom.penup()
tom.goto(-50, -175)
tom.pendown()
tom.color("black")
tom.begin_fill()
tom.circle(25)
tom.end_fill()
tom.penup()
tom.goto(125, -175)
tom.pendown()
tom.begin_fill()
tom.circle(25)
tom.end_fill()

turtle.exitonclick()