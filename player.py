from turtle import Turtle

starting_pos = (0, -280)
dist = 10
end_ycor = 200


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(starting_pos)
        self.setheading(90)

    def go_up(self):
        self.forward(dist)

    def next_level(self):
        self.goto(starting_pos)
        self.setheading(90)

