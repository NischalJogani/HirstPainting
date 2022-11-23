# Todo 2: Import Random, DotSystem Turtle and Screen
import random
import turtle
from turtle import Turtle, Screen
from dot_system import DotSystem


# Todo 3: Make turtle object, screen object and dotsystem object
tim = Turtle()
dot_system = DotSystem(tim)
screen = Screen()
rgb_color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162),
                  (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47),
                  (55, 108, 89), (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36),
                  (228, 173, 166), (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190),
                  (51, 149, 193), (166, 200, 213)]
turtle.colormode(255)
tim.speed(0)


# Todo 4: For loop
for row in range(11):
    # Another for loop to make 20*20 dotted grid
    for column in range(12):
        # Chooses a random color from the color list and sets it as the dot color
        color = random.choice(rgb_color_list)
        # Makes a dot using make dot function
        dot_system.make_dot(color)
    # Changes the row of turtle
    dot_system.change_row()

screen.exitonclick()
