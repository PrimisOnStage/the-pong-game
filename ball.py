import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        t.Turtle.__init__(self)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movey = 1
        self.movex = 2

    def move_it(self):
        x = self.xcor() + self.movex
        y = self.ycor() + self.movey
        self.goto(x, y)



    def bouncex(self):
        self.movex *=-1
    def bouncey(self):
        self.movey *=-1
