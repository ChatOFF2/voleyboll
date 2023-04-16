import turtle
import random


class ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.color("blue")
        new_gradus = random.randint(0, 360)
        self.setheading(new_gradus)



    def move_ball(self):
        self.forward(10)

    def boll_tern(self):
        new_gradus = random.randint(0, 360)
        self.setheading(new_gradus)
