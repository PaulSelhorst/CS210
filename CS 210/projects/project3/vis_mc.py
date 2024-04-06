import turtle
from mc import pi_mc

turtle.speed('fastest')
def mc_vis(num_darts: int):
    """
    Visualize the Monte Carlo method for approximating pi.

    num_darts is the number of darts to throw.
    """
    import random
    import math

    random.seed(42)
    

    num_darts_in_circle = 0

    for n in range(num_darts):
        x = random.random()
        if random.random()>.5:
            x = x - 1
        y = random.random()
        if random.random()>.5:
            y = y - 1

        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            num_darts_in_circle += 1
            turtle.color("blue")
            turtle.penup()
            turtle.goto(x*200, y*200)
            turtle.pendown()
            turtle.dot()

        else:
            turtle.color("red")
            turtle.penup()
            turtle.goto(x*200, y*200)
            turtle.pendown()
            turtle.dot()

    pi = num_darts_in_circle / num_darts * 4

    return pi

turtle.penup()
turtle.goto(0,500)
turtle.pendown()
turtle.goto(0,-500)
turtle.penup()
turtle.goto(500,0)
turtle.pendown()
turtle.goto(-500,0)
turtle.penup()


mc_vis(1000)
turtle.done()