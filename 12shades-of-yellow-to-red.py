#Name: Ishika Soni
#Email: ishika.soni97@myhunter.cuny.edu
#Date: September 30, 2021
#This program draws two transitions from shades of yellow to red by moving
#forward 10 steps each.

import turtle

turtle.colormode(255)
tess = turtle.Turtle()

def transition():
    for i in range(0,255,10):
        tess.forward(10)
        tess.pensize(i)
        tess.color(255,255-i,0)

transition()
tess.penup()
tess.pensize(0)
tess.color(0,0,0)
tess.backward(260)
tess.right(90)
tess.pendown()
transition()
