import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    chance = random.randint(1, 6)
    if chance == 2:
        cars.create_car()
    if score.level % 3 == 0 or (score.level - 1) % 3 == 0 or (score.level - 2) % 3 == 0 and (score.level - 2) / 3 != 0:
        for i in range(0, int(score.level/3)):
            le_chance = random.randint(1, 6)
            if le_chance == 2:
                cars.create_car()
    if (score.level - 1) % 3 == 0:
        for i in range(0, int((score.level - 1)/3)):
            le_chance = random.randint(1, 6)
            if le_chance == 2:
                cars.create_car()
    if (score.level - 2) % 3 == 0 and (score.level - 2) / 3 != 0:
        for i in range(0, int((score.level - 1)/3)):
            le_chance = random.randint(1, 6)
            if le_chance == 2:
                cars.create_car()
    cars.move()

    for car in cars.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() == 280:
        player.next_level()
        cars.next_level()
        score.inc_levels()


screen.exitonclick()

