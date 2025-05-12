from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("red")
        self.speed('fastest')
        random_X=random.randint(-280, 280)
        random_y=random.randint(-280, 280)
        self.goto(random_X,random_y)
        self.refresh()


    def refresh(self):
        random_X=random.randint(-280, 280)
        random_y=random.randint(-280, 280)
        self.goto(random_X,random_y)
