from turtle import *
from random import *
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.8,0.8)
        self.color("red")
        self.speed(0)
        self.repos()

    def repos(self):

        rx=randint(-280,280)
        ry=randint(-280,280)
        self.goto(rx,ry)

