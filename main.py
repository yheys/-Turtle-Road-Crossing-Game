import time
from turtle import Screen
from player import Player
from scorebord import Score_Bord
from car import Car


screen=Screen()
screen.screensize(600,600,"white")
screen.tracer(0)

player=Player()
level=Score_Bord()
car=Car()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.new_car()
    car.move()
    if player.ycor()>=280:
        level.updated_level()
        player.next_level()
        car.next_move()
    for one_car in car.all_cars:
        if one_car.distance(player)<20:
            game_is_on=False
            level.end()

































screen.exitonclick()