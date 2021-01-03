import random
from turtle import Turtle, Screen
import turtle

screen = Screen()
import time
turtle.colormode(255)

color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176),
              (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50),
              (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86),
              (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161),
              (152, 213, 190), (242, 205, 8), (89, 48, 31)]
gap = []
for i in range(-230,250,50):
    gap.append(i)

print(gap)

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            c = random.choice(color_list)
            new_car.color(c)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300,random.choice(gap))
            self.all_cars.append(new_car)



    def random_c(self):
        k = random.choice(color_list)
        return k

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
            self.car_speed += MOVE_INCREMENT