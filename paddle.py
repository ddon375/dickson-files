from turtle import Turtle


class Paddle(Turtle,):
    """This class creates a new paddle given the coordinates it should go to"""
    def __init__(self, coordinate):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(coordinate)

    def go_up(self):
        """This method moves the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """This method moves the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

# i was just trying to see if this method is possible and indeed it is but it took me a long time to get it to work.
# class RightPaddle:
#     def __init__(self):
#         self.rightist = []
#
#     def add_turtle(self):
#         ycor = 50
#         for i in range(5):
#             self.squares = Turtle()
#             self.squares.penup()
#             self.squares.shape("square")
#             self.squares.color("white")
#             self.squares.goto(360, ycor)
#             ycor -= 20
#             self.rightist.append(self.squares)
#             print("yes")
#
#     def move_up(self):
#         for squares in range(4, 0, -1):
#             xcor = self.rightist[squares-1].xcor()
#             ycor = self.rightist[squares-1].ycor()
#             self.rightist[squares].goto(xcor, ycor)
#         self.rightist[0].setheading(90)
#         self.rightist[0].forward(20)





