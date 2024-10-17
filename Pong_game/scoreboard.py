from turtle import Turtle

class ScoreBoard(Turtle):
    """ The Scoreboard creates the object that have attributes and method like  update_score(self), Update_L_score(self), Update_R_score(self):"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.L_score = 0
        self.R_score = 0
        self.hideturtle()
        self.penup()
        self.update_score()
    
        
    def update_score(self):
         """This method is used for to print the L_score and R_score on its specific position """
         self.goto(-50,230)
         self.write(self.L_score,font=("vardana",40,"normal"),align="center")
         self.goto(50,230)
         self.write(self.R_score,font=("vardana",40,"normal"),align="center")
    
    # def divider(self):                    ///////////  This is the function for create a divider in between the score bord.
    #     self.color("white")
    #     self.hideturtle()
    #     self.penup()
    #     self.goto(0,280)
    #     self.right(90)
    #     for i in range(0,400,20):
    #         self.pendown()
    #         self.forward(50)
    #         self.penup()
    #         self.forward(50)
    def Update_L_score(self):
        """This method help us to increase the Left side score"""
        self.L_score += 1
        self.clear()
        self.update_score()
    def Update_R_score(self):
        """This method help us to increase the Right side score"""
        self.R_score += 1
        self.clear()
        self.update_score()