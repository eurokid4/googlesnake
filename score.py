from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.high_score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.upds()

    def incrsco(self):
        self.score+=1
        self.clear()
        self.upds()

    def upds(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Sans",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.color("#EE4B2B")
        self.write(f'''GAME OVER!!!:(
Click to exit''',align="center",font=("Arial",24,"bold"))
