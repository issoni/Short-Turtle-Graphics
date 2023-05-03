#Name: Ishika Soni
#Email: ishika.soni97@myhunter.cuny.edu
#Date: September 29, 2021
#This program draws shades of yellow in the shape of a pseudo-heart.

import turtle

turtle.colormode(255)
tess = turtle.Turtle()

def paintYellow():
    for i in range(0,255,10):
        tess.forward(10)
        tess.pensize(i)
        tess.color(i,i,0)

tess.left(60)
paintYellow()
tess.penup()
tess.pensize(0)
tess.color(0,0,0)
tess.backward(260)
tess.left(60)
tess.pendown()
paintYellow()


