#Name: Ishika Soni
#Email: ishika.soni97@myhunter.cuny.edu
#Date: October 4, 2021
#This program asks the user for a 6-digit hex number and uses it as the hex code
#to stamp 4 turtles of that color into a square.

import turtle

mess = input("Please enter a 6-digit Hexadecimal number: ")

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("#"+mess)

for i in range(4):
    alex.stamp()
    alex.left(90)
    alex.forward(100)


