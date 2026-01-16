import turtle as button

button.hideturtle()

wn = button.Screen()
wn.bgpic("background1")

#create the button
button.speed(10000000) # Set speed before drawing


button = button.Turtle()
button.shape("square")
button.penup()
button.color("grey")
button.shapesize(0.3)
button.goto(385, -53)




wn.listen()
wn.mainloop()