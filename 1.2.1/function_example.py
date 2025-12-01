#import turtle
import turtle as trtl

#make a turtle
james = trtl.Turtle()




james.forward(60)


def drawSquare():
    for sides in range(4):
        james.forward(30)
        james.right(90)

        

drawSquare()
wn = trtl.Screen()
drawSquare()
#Goal: to draw squares with a turtle