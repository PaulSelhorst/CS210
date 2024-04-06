import turtle

# Create a turtle object
duck = turtle.Turtle()

# Set the turtle's speed
duck.speed(20)

# Draw the body of the duck

duck.penup()
duck.goto(-150,50)
duck.circle(60,45)
duck.pendown()
duck.begin_fill()
duck.fillcolor("#fff68f")
duck.circle(80,270)
duck.right(105)
duck.circle(100,120)
duck.forward(40)
duck.circle(200,30)
duck.forward(40)
duck.circle(180,30)
duck.forward(40)
duck.circle(200,20)
duck.forward(50)
duck.circle(180,20)
duck.forward(30)
for i in range(30):
    duck.forward(1)
    duck.left(2)
duck.left(84.4)
duck.circle(-300,62.3)
duck.end_fill()
duck.penup()

#Beak
duck.goto(-222,78)
duck.circle(30,20)
duck.pendown()
duck.begin_fill()
duck.fillcolor("#ffa738")
duck.right(140)
duck.circle(25,150)
duck.left(40)
duck.circle(-30,75)
duck.circle(3,220)
duck.right(20)
duck.circle(-100,20)
duck.right(150)
duck.circle(120,20)
duck.left(130)
duck.circle(120,31)
duck.end_fill()
duck.penup()

duck.color("#e0820b")
duck.goto(-235,118)
duck.pendown()
duck.begin_fill()
duck.fillcolor("#e0820b")
duck.circle(2)
duck.end_fill()
duck.penup()

#Eye
duck.color("black")
duck.goto(-190,138)
duck.begin_fill()
duck.fillcolor("black")
duck.circle(20)
duck.end_fill()


# Hide the turtle
duck.hideturtle()

# Keep the window open
turtle.done()
