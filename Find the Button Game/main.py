import turtle

# Screen setup
wn = turtle.Screen()
current_bg = 1
wn.bgpic("background1") 

# Tracking function
def change_background(x, y):
    global current_bg
    current_bg += 1
    if current_bg > 6:  # Reset to 1 after background 6
        current_bg = 1
    
    new_bg = f"background{current_bg}.gif"
    wn.bgpic(new_bg)
    print(f"Switched to {new_bg}")

# Button setup
button = turtle.Turtle()
button.shape("square")
button.penup()
button.color("grey")
button.shapesize(2)  # Made larger for easier clicking
button.goto(300, -50)

# Bind the click event to the button turtle
button.onclick(change_background)

wn.listen()
wn.mainloop()
