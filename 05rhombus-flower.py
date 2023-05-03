#Name: Ishika Soni
#Email: ishika.soni97@myhunter.cuny.edu
#Date: September 21, 2021
#This program draws a rhombus flower.

import turtle 
wn = turtle.Screen() #set up the window and its attributes
wn.bgcolor("orange")

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("white")
alex.fillcolor("green")
alex.pensize(3)

for i in range(6):
    alex.forward(100)
    alex.left(45)
    alex.forward(100)
    alex.left(135)
    alex.stamp()
    alex.forward(100)
    alex.left(45)
    alex.forward(100)
    alex.left(75)

