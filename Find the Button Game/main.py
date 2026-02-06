import turtle
import random
#variable setup
score=0
font_setup = ("Arial", 20, "bold")
current_bg = 1

# Screen setup
wn = turtle.Screen()
wn.bgpic("background1.gif")

#score writer setup
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(200, 250)
score_writer.write(f"Score: {score}", font=font_setup)

timer = 200
counter_interval = 1000   #1000 represents 1 second
timer_up = False
turtle.hideturtle()

button_positions = [
    (-381, -51), #1
    (168, -59), #2
    (20, 0), #3
    (94.5, -15), #4
    (10, -100), #5
    (-200, 100), #6
    (-237, -20), #7 new photos
    (-135, 144), #8
    (150, 50), #9
    (200, -33), #10
    (300, -75), #11
    (-250, 0), #12
    (-900, -100) #13
]

#score
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=font_setup)

counter =  turtle.Turtle()

def counter_setup():
  counter.pendown()
  counter.forward(-300)
  counter.left(90)
  counter.forward(250)
  counter.right(90)
  counter.hideturtle()
turtle.speed(0)
#start countdown and update
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


def draw_confetti(amount, x_loc, y_loc):

    # Set up a temporary turtle for confetti
    effect = turtle.Turtle()
    effect.hideturtle()
    effect.speed(0)
    effect.penup()

    #Add confetti (row 5)
    for i in range(amount):

        color_list = ["red", "blue", "green", "yellow", "purple"]


        if i % 2 == 0:
            effect.color(random.choice(color_list))
        else:
            effect.color("orange")

        effect.goto(x_loc + random.randint(-20, 20), y_loc + random.randint(-20, 20))
        effect.dot(5)

    effect.clear()  #Clear confetti for next round

def change_background(x, y):
    draw_confetti(5, x, y)

    update_score()
    global current_bg
    current_bg += 1

    # Reset to 1 if player goes past 13
    if current_bg > 13:
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
button.shapesize(0.1)
button.goto(button_positions[0])

# Bind click event to the button turtle
button.onclick(change_background)
wn.ontimer(countdown, counter_interval)
counter_setup()
wn.listen()
wn.mainloop()