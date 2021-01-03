from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.color("black")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level : {self.score} ", align="center", font=FONT)

    def finish_point(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f" Game Over ", align="center", font=FONT)


