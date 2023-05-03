#Name: Ishika Soni
#Email: ishika.soni97@myhunter.cuny.edu
#Date: November 7, 2021
#This program returns a turtle tree.

import turtle

def setUp():
    """
    Takes no parameters, and simply sets up the turtle, returning to caller.
    Here you should:
        1. Instiantiate the turtle,
        2. optionally hide the turtle (use .hideturtle())
        3. set the heading to 90 (which will face the turtle upwards)
        4. set the speed (t.speed(speed=0), you will want this)
        5. return the turtle to the calling function.
    """

    tess = turtle.Turtle()
    tess.hideturtle()
    tess.left(90)
    tess.speed(speed=0)
    return tess
    

def fractalLeft(t,distance,i):
    """
    Takes three parameters: a turtle t, distance 'distance', and i, the
    color value. This function does the following: if the distance is greater than 10,
    it will:
        1. Set the value of i to be i % 255,
        2. set the color of the turtle to be the value of i in the green channel (0,i,0)
        3. turn left 30 degrees
        4. move forward 'distance' steps
        5. stamp the turtle
        6. set the value of newDistance to distance-5
        7. call fractalLeft with the parameters t, newDistance, i+25
        8. move backward by 'distance' steps, NOT newDistance,
        9. turn right 30 degrees
        10. call fractalRight with parameters t, newDistance, i+25
    """
    if distance > 10:
        i = i % 255
        t.color(0, i, 0)
        t.left(30)
        t.forward(distance)
        t.stamp()
        newDistance = distance - 5
        fractalLeft(t, newDistance, i+25)
        t.backward(distance)
        t.right(30)
        fractalRight(t, newDistance, i+25)
    

def fractalRight(t,distance,i):
    """
    Takes three parameters: a turtle t, distance 'distance', and i, the
    color value. This function does the following: if the distance is greater than 10,
    it will:
        1. Set the value of i to be i % 255,
        2. set the color of the turtle to be the value of i in the green channel (0,i,0)
        3. turn right 30 degrees
        4. move forward 'distance' steps
        5. stamp the turtle
        6. set the value of newDistance to distance-5
        7. call fractalRight with the parameters t, newDistance, i+25
        8. move backward by 'distance' steps, NOT newDistance,
        9. turn left 30 degrees
        10. call fractalLeft with parameters t, newDistance, i+25
    """
    if distance > 10:
        i = i % 255
        t.color(0, i, 0)
        t.right(30)
        t.forward(distance)
        t.stamp()
        newDistance = distance - 5
        fractalRight(t, newDistance, i+25)
        t.backward(distance)
        t.left(30)
        fractalLeft(t, newDistance, i+25)




############################################################################################

    
def main():
    ###################################
    ###    DON'T CHANGE THIS: vvv   ###
    ###################################
    t = setUp()
    turtle.colormode(255)
    turtle.bgcolor("khaki")
    t.forward(50)
    fractalRight(t,50,0)
    fractalLeft(t,50,0)

if __name__ == "__main__":
    main()
