import random
from turtle import Turtle

colors = ("blue", "green", "red", "violet", "yellow", "cyan")
level_up_speed = 5
move_increment = 10


class CarManager:

    def __init__(self):
        self.all_car = []
        self.speed = move_increment

    def create_car(self):

        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(colors))
        new_car.setheading(180)
        new_car.goto(x=300, y=random.randint(-250, 250))
        self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            car.forward(self.speed)

    def next_level(self):
        self.speed += level_up_speed



