from turtle import Turtle


class Scoreboard(Turtle):
    """creates the scoreboard given the coordinate of the score it should go to"""
    def __init__(self, position):
        super().__init__()
        self.player_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)

    def write_score(self):
        """writes the score at the coordinate you've chosen"""
        self.clear()
        self.write(f"{self.player_score}", False, "left", ("arial", 50, "normal"))
