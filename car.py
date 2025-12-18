from turtle import Turtle
import random

color=["red","green","blue","black","orange","yellow",]
starting=(300,random.randint(-280,280))
num=random.randint(3,10)
CAR_SPEED=5

class Car:
    def __init__(self):
        self.all_cars=[]
        self.CAR_SPEED=5

    def new_car(self):
        random_num=random.randint(1,10)
        if random_num==1:
            new=Turtle("square")
            new.color(random.choice(color))
            new.shapesize(1, 2)
            new.penup()
            new.goto(350,random.randint(-280,280))
            self.all_cars.append(new)

    def move(self):
        for car in self.all_cars:
            car.bk(self.CAR_SPEED)
    def next_move(self):
        self.CAR_SPEED+=5












