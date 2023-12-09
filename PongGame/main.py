from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid= 5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
#screen.onkey(go_up,"Up")
#screen.onkey(go_up,"Up")

#l_paddle = Paddle(350,0)
#r_paddle = Paddle(-350,0)
l_paddle = Paddle()
l_paddle.create_paddle(350,0)
r_paddle = Paddle()
r_paddle.create_paddle(-350,0)
ball = Ball()



game_is_on = True

while game_is_on:
    time.sleep(.01)
    screen.update()
    ball.move()
    


screen.exitonclick()
