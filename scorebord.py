from turtle import Turtle

class Score_Bord(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-290,290)
        self.score=0
        self.write(f" level {self.score}",False,"center",("Courier",20,"normal"))

    def updated_level(self):
        self.score += 1
        self.clear()
        self.write(f" level {self.score}", False, "center", ("Courier", 20, "normal"))

    def end(self):
        self.goto(0,0)
        self.write(f" Game Over", False, "center", ("Courier", 20, "normal"))
