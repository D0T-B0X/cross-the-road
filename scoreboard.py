from turtle import Turtle
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=265)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def inc_levels(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=("Courier", 30, "bold"))
        self.goto(x=0, y=-18)
        self.write(f"Score: {self.level}", align="center", font=FONT)
