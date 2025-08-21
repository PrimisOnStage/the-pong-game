import turtle as t
from scoreboard import GameScoreboard
from ball import Ball
import gui
from gui import *

#Screen Setup
sc = t.Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Pong")
sc.listen()
sc.tracer(0)

#Paddle Setup
p1 = gui.Paddle(350)
p2 = gui.Paddle(-350)

#Ball Setup
ball = Ball()
score = GameScoreboard()

sc.onkey(p1.go_up, "Up")
sc.onkey(p1.go_down, "Down")
sc.onkey(p2.go_up, "w")
sc.onkey(p2.go_down, "s")

game = True
while game:
    sc.update()

    if ball.xcor()>380 or ball.xcor()<-380:
        ball.bouncex()
        if ball.xcor() > 380:
            score.scorel += 1
        if ball.xcor() < -380:
            score.scorer += 1
        score.update()
        ball.goto(0,0)


    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bouncey()

    if ball.distance(p1)<50 and ball.xcor()>340:
        ball.bouncex()

    if ball.distance(p2)<50 and ball.xcor()<-340:
        ball.bouncex()


    sc.tracer(1)
    ball.move_it()
    sc.tracer(0)







sc.exitonclick()