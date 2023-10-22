from turtle import *

STARTING_POSITIONS=[(-20,0),(-40,0),(-60,0),(-80,0)]
class sNaKe:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,pos):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(pos)
        self.segments.append(s)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for segnum in range(len(self.segments)-1,0,-1):
            nex=self.segments[segnum-1].xcor()
            ney=self.segments[segnum-1].ycor()
            self.segments[segnum].goto(nex,ney)
        self.segments[0].forward(20)  

    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].seth(270)

    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].seth(0)

    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].seth(180)
