from turtle import Turtle

class Paddle(Turtle):
    """ This is the paddle class having attributes and methods like go_up() , go_down() """
    def __init__(self,position_x,position_y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)   
        self.penup()
        self.color("white")
        self.goto(position_x,position_y)
    def go_up(self):
        """This Method help the Paddle to gho upwards direction """
        new_y = (self.ycor() + 50)  
        self.goto(self.xcor(),new_y )
       # Move 20 units upwards
    def go_down(self):
         """This Method help the Paddle to gho downwards direction """
         new_y  =( self.ycor() - 50 )
         self.goto(self.xcor(),new_y)
       # Move 20 units upwards
    
    