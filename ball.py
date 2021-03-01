from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.y_rand = random.randint(-250,250)
        self.x_increase = 10
        self.y_increase = 10
        self.choice = random.randint(1, 2)
        if self.choice == 1:
            self.y_increase = -10
        self.goto(0, self.y_rand)

    def current_x_position(self):
        """this method returns the current x-coordinate"""
        xcor = self.xcor()
        return xcor

    def current_y_position(self):
        """this method returns the current y-coordinate"""
        ycor = self.ycor()
        return ycor

    def move_ball(self):
        """this moves the ball upwards from middle of the screen to the edge of the screen"""
        self.goto(self.current_x_position() + self.x_increase, self.current_y_position() + self.y_increase)

    def bounce_back(self):
        self.y_increase *= -1
