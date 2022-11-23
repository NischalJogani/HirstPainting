# Todo 1: Make dotsystem class
class DotSystem:

    # Todo 1#: Init function
    def __init__(self, turtle):
        # Has the turtle object
        self.obj = turtle
        # Defines the x and y cor of turtle object
        self.xcor = -215
        self.ycor = -200
        self.obj.penup()
        self.obj.setpos(self.xcor, self.ycor)
        self.obj.pendown()

    # Todo 2#: Make a dot making function
    def make_dot(self, color):
        # Makes a dot
        self.obj.dot(10, color)
        # Pen Up
        self.obj.penup()
        # Move forward
        self.obj.forward(40)
        # Pen down
        self.obj.pendown()

    # Todo 3#: Change row function
    def change_row(self):
        # Changes the y coordinate
        self.ycor += 40
        # Update's the turtle object's position
        self.obj.penup()
        self.obj.setpos(self.xcor, self.ycor)
        self.obj.pendown()
