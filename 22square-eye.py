#Name: Ishika Soni
#Email: ishika.soni97@myhunter.cuny.edu
#Date: October 15, 2021
#This program draws a spiral of squares using turtles.

import turtle

tess = turtle.Turtle()
turtle.colormode(255)
tess.speed(0)
tess.pensize(5)

wn = turtle.Screen() #set up the window and its attributes
wn.bgcolor("khaki")

for i in range(36):
    tess.pencolor(0, i * 7, 0)
    tess.forward(10)
    tess.left(10)
    for i in range(4):
        tess.left(90)
        tess.forward(300)
        tess.backward(50)
