from turtle import Turtle

class Ball(Turtle):
    """This is the Ball class having attributes and method like move(self), bounce_y(self), bounce_x(self), increase(self) """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.increase_S = 0.1
    def move(self):
        """ This method is used for Move the ball by one step"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        """ This method help to change the value of y_move by multypling -1 si that's change the direction in reverse order"""
        self.y_move *= -1
    def bounce_x(self):
        """ This method help to change the value of x_move by multypling -1 so that's change the direction in reverse order"""
        self.x_move *= -1
    def increase(self):
        """ This method help to increase the valve od variable increase_S by multiplying 0.9 """
        self.increase_S *= 0.9