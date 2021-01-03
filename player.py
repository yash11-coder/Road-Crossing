from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.player()

    def player(self):
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.go_to_start()
        self.left(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() == 280:
            return True
        else:
            return False





