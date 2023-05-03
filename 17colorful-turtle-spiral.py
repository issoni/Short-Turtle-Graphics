#Name: Ishika Soni
#Email: ishika.soni97@myhunter.cuny.edu
#Date: October 7, 2021
#This program draws out the stamps of the turtle using the number given by the
#user.

import turtle

num = input("Enter the number of stamps the turtle will print: ")
num = int(num)
tess = turtle.Turtle()
turtle.colormode(255)
tess.shape('circle')
tess.penup()
steps = 10
red = 186
green = 164
blue = 145 
tess.color(red, green, blue)

for i in range(num):
    tess.stamp()
    steps += 2
    if red + 3 <= 255 and green + 3 <= 255 and blue + 3 <= 255:
        red += 3
        green += 3
        blue += 3
    tess.color(red, green, blue)
    tess.forward(steps)
    tess.right(24)


