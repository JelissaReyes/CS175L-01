#CS 175L-01
#Jelissa Reyes
#Chapter 4 Turtle Graphics STOP Sign 

import math
import turtle

#Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

turtle.color("black","red")

#make the stop sign
turtle.penup()
turtle.goto(-50,145)
turtle.pendown()
turtle.begin_fill()


for x in range(8):
    turtle.forward(100)
    turtle.right(45)
turtle.end_fill()

#font
turtle.color("white")
turtle.penup()
turtle.goto(0,0)
turtle.write("Stop", align = "center", font=("Calibri", 35, "bold"))
