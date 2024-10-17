from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard  #  Imporing Required module

# Screen Functionality
screen = Screen()
screen.title("PONG GAME")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# creating objects
r_paddle = Paddle(365,0)
l_paddle = Paddle(-365,0)
ball = Ball()
score = ScoreBoard()

# screen function How to controll the Paddle. 
# 1 - for Right Paddle use UP_arrow_key for move upwards and for down use down_arrow_key.

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
# 2 - for Left Paddle "w" for move upwards and for down use "s" .
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    
    screen.update() # update the screen every time for smooth animation.
    time.sleep(ball.increase_S)# wiat and increases the speed every time when the ball hit the paddle.
   
    ball.move() # for continusly moving ball.
    if  ball.ycor() > 280 or ball.ycor() < -280:
       # condition check is the ball under the roof and land and when it hit any of them then back to reverse.
       ball.bounce_y()
    if ball.distance(r_paddle)<70 and ball.xcor() > 330 or ball.distance(l_paddle)< 70 and ball.xcor() < -330:
        # condition for to know is the ball hit the paddle or not 
        ball.increase()
        ball.bounce_x()
    if ball.xcor() > 400 :
        #This condition check if the ball is miss by the right paddle then increase the score of left_person.
        score.Update_L_score()
        ball.goto(0,0)
        time.sleep(0.5)
        ball.move()
    elif ball.xcor() < -400 :
        #This condition check if the ball is miss by the Left paddle then increase the score of Right_person.
        score.Update_R_score()
        ball.goto(0,0)
        time.sleep(0.5)
        ball.move()

screen.exitonclick()