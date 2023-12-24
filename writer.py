import turtle
class Writer(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
    def write_state(self,x,y,text):
        self.goto(x,y)
        self.write(text,font=('Arial',8) )