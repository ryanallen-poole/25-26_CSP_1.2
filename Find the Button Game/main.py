import turtle
#variable setup
score=0
font_setup = ("Arial", 20, "bold")
current_bg = 1

# Screen setup
wn = turtle.Screen()
current_bg = 1
wn.bgpic("background1.gif")

#score writer setup
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(200, 250) # Adjusted to fit standard screens
score_writer.write(f"Score: {score}", font=font_setup)

button_positions = [
    (-381, -50),
    (167, -59),
    (20, 0),
    (94.5, -15),
    (10, -100),
    (-200, 100)
]


# Tracking function
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=font_setup)

def change_background(x, y):
    update_score()
    global current_bg
    current_bg += 1

    # Reset to 1 if we go past 6
    if current_bg > 6:
        current_bg = 1

    #update the background image
    new_bg = f"background{current_bg}.gif"
    wn.bgpic(new_bg)

    #move the button
    new_pos = button_positions[current_bg - 1]
    button.hideturtle()
    button.goto(new_pos)
    button.showturtle()
    print(f"Switched to {new_bg} and moved to {new_pos}")


# Button setup
button = turtle.Turtle()
button.shape("square")
button.penup()
button.color("grey")
button.shapesize(0.2)  # Made larger for easier clicking
button.goto(button_positions[0])

# Bind click event to the button turtle
button.onclick(change_background)

wn.listen()
wn.mainloop()