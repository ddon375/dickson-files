from turtle import Screen
from paddle import Paddle #RightPaddle
from turtle import Turtle
from ball import Ball
import time
from scoreboard import Scoreboard

# This is the code that creates my screen
my_screen = Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor("black")
my_screen.title("Pong game")
my_screen.tracer(0)
my_screen.listen()

# This is where i initialised my classes
right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
left_scoreboard = Scoreboard((-200, 230))
right_scoreboard = Scoreboard((200, 230))
left_scoreboard.write_score()
right_scoreboard.write_score()

# The following code controls the movement of the paddle
my_screen.onkey(right_paddle.go_up, "Up")
my_screen.onkey(right_paddle.go_down, "Down")
my_screen.onkey(left_paddle.go_up, "w")
my_screen.onkey(left_paddle.go_down, "s")

# creates the divide line
line_turtle = Turtle()
line_turtle.hideturtle()
line_turtle.color("white")
line_turtle.penup()
line_turtle.goto(0, -290)
line_turtle.pencolor("white")
line_turtle.setheading(90)
for i in range(20):
    line_turtle.pendown()
    line_turtle.forward(20)
    line_turtle.penup()
    line_turtle.forward(10)

# the movement on the screen starts here
game_on = True
speed = 0.1
half = 0.9
while game_on:
    my_screen.update()
    time.sleep(speed)
    ball.move_ball()
    # detects collision with the upper
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_back()

    #  checks if the ball has made contact with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        if ball.y_increase == -10 and ball.x_increase == 10:
            ball.x_increase = -10
            speed *= half
        elif ball.y_increase == 10 and ball.x_increase == 10:
            ball.x_increase = -10
            speed *= half

    # checks if ball has made contact with the left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -350:
        if ball.y_increase == -10 and ball.x_increase == -10:
            ball.x_increase = 10
            speed *= half
        elif ball.y_increase == 10 and ball.x_increase == -10:
            ball.x_increase = 10
            speed *= half

    # check if the ball misses the right paddle
    if ball.xcor() == 410:
        left_scoreboard.player_score += 1
        left_scoreboard.write_score()
        speed = 0.1
        ball = Ball()
        ball.x_increase = -10

    # check if the ball misses the left paddle
    if ball.xcor() == -410:
        right_scoreboard.player_score += 1
        right_scoreboard.write_score()
        speed = 0.1
        ball = Ball()

my_screen.exitonclick()
