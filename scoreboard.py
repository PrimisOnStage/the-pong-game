import turtle as t
class GameScoreboard(t.Turtle):
    def __init__(self):
        t.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.goto(-100, 200)
        self.color('white')
        self.scorer = 0
        self.scorel = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"LEFT:{self.scorel} | RIGHT:{self.scorer}")
