import turtle as t

class Paddle(t.Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x_position, 0)
        self.setheading(90)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)




