from ctypes import alignment
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",15,"normal")

tim = Turtle()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("lime")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        tim.color("white")
        tim.hideturtle()
        tim.penup()
        tim.goto(-295, 295)
        tim.pendown()
        for i in range(0,4):
            tim.forward(585)
            tim.right(90)
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    