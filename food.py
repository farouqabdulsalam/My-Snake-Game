from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
# the shapes in python turtle arrow , blank , circle , classic , square , triangle , turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

# moves the food to a random position
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
