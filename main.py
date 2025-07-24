import turtle as t

import gui
from gui import *

sc = t.Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Pong")
sc.listen()
sc.tracer(0)
p1 = gui.Paddle(350)
p2 = gui.Paddle(-350)
sc.tracer(1)

sc.onkey(p1.go_up, "Up")
sc.onkey(p1.go_down, "Down")
sc.onkey(p2.go_up, "w")
sc.onkey(p2.go_down, "s")









sc.exitonclick()