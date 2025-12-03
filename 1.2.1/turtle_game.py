# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "purple"

#-----initialize turtle-----
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

#-----game functions--------
#get a score boost,
def spot_clicked(x,y):
    #move the turtle to a random location
    newX = rand.randint(-450,450)
    newY = rand.randint(-450,450)
    meowl.goto(newX,newY)


#-----events----------------
meowl.onclick(spot_clicked)

wn = trtl.Screen()
wn.mainloop()