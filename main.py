import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player =Player()
screen.listen()
screen.onkey(player.up, "Up")
car_manager = CarManager()
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.cars()
    car_manager.move()





    for car in car_manager.all_cars:
        if car.distance(player)<20:
            score.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        score.finish_point()
        car_manager.level_up()
        player.go_to_start()



screen.exitonclick()
