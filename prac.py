import turtle
import time

scr=turtle.Screen()
scr.setup(600,600)
scr.bgcolor("black")
scr.title("C̶l̶a̶s̶s̶i̶c̶ snake game")
scr.tracer(0)

# seg1=turtle.Turtle("square")
# seg1.color("white")
# seg1.goto(0,0)


# seg2=turtle.Turtle("square")
# seg2.color("white")
# seg2.goto(-20,0)


# seg3=turtle.Turtle("square")
# seg3.color("white")
# seg3.goto(-40,0)

segs=[]
startpos=[0,-20,-40]

for position in startpos:
    snakeseg=turtle.Turtle("square")
    snakeseg.color("white")
    snakeseg.penup()
    snakeseg.goto(position,0)
    segs.append(snakeseg)

isgamestarted=True
while isgamestarted:
    # for snakeseg in segs:
    #     snakeseg.forward(20)

    for segnum in range(len(segs)-1,0,-1):
        nex=segs[segnum-1].xcor()
        ney=segs[segnum-1].ycor()
        segs[segnum].goto(nex,ney)
    segs[0].forward(20)    
    scr.update()
    time.sleep(0.2)

scr.exitonclick()