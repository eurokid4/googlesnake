import turtle
import time
from score import Score
from snake import sNaKe
from food import food

sc=turtle.Screen()
sc.setup(600,600)
sc.bgcolor("black")
sc.title("uwu")
# sc.tracer(0)
s=sNaKe()
f=food()
sco=Score()
sc.listen()
sc.onkey(s.up,"Up")
sc.onkey(s.down,"Down")
sc.onkey(s.left,"Left")
sc.onkey(s.right,"Right")
sc.tracer(0)
igs=True
while igs:
    s.move()
    sc.update()

    time.sleep(0.3)
    if s.segments[0].distance(f)<10:
        s.extend()
        f.repos()
        sco.incrsco()


    if s.segments[0].xcor()>280 or s.segments[0].xcor()<-280 or s.segments[0].ycor()>280 or s.segments[0].ycor()<-280:
        igs=False
        sco.game_over()

    for i in s.segments:
        if i==s.segments[0]:
            pass
        elif s.segments[0].distance(i)<10:
            igs=False
            sc.game_over()





sc.exitonclick()