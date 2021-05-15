

# first we need to import modules 

import turtle
from turtle import *
from random import randint


# Drawing shape
# I prefer doing this with a function

def main():
    # set background color of turtle
    bgcolor('black')

    # create a variable called H
    H = 1

    # set speed of turtle
    speed(0)
    # I prefer hiding turtle during drawing
    hideturtle()


    # NOw I have to use while loop 
    while H < 350:
        # set up random rgb color to your drawing
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

        # set pen color
        colormode(255)
        pencolor(r,g,b)

        # now pen up your turtle
        penup()
        forward(H)
        right(95)
        # pendown()

        forward(H)
        dot()
        H = H + 1

    done()

# call main test
main()

# now run your code using terminal or and other IDE
# Look if we change the line style to dot()



# Lets is change the turning angle 

'''
Thank you for watching !
Please subscribe my Channel
'''








