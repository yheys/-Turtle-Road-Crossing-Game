from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -300)
        self.left(90)


    def move(self):
        new_y=self.ycor() +20
        self.goto(0,new_y)

    def next_level(self):
         self.goto(0,-300)
