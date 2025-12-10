#1.2.2 File
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
spot_color = "purple"
score = 0
font_setup = ("Arial", 20, "normal")

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

bg_color = "lightblue"
#-----initialize turtle-----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("What is your name?")


counter =  trtl.Turtle()
# Score turtle
score_writer = trtl.Turtle()
score_writer.penup()

# Turtle to draw a box
box_turtle = trtl.Turtle()
box_turtle.penup()

# Shape turtle
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

#list of colors
colors = ["red", "maroon", "pink", "purple", "white", "blue", "yellow"]

#list of sizes for the shape
sizes = [2, 2.5, 3, 4, 5, 5.5, 6]

#-----game functions--------
# Draw the box for the score
def scoreBox():
    box_turtle.goto(275, 325)
    box_turtle.pendown()

    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)

    score_writer.penup()
    score_writer.goto(300, 332)

    score_writer.hideturtle()
    box_turtle.hideturtle()

# Get a score boost, move the turtle randomly
def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_position()
        # Call the new functions here when the spot is clicked
        change_color_randomly(meowl, colors)
        change_size_randomly(meowl, sizes)
    else:
        meowl.hideturtle()

def change_position():
    newX = rand.randint(-300, 300)
    newY = rand.randint(-300, 300)
    meowl.goto(newX, newY)
    update_score()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def counter_setup():
  counter.pendown()
  counter.forward(-300)
  counter.left(90)
  counter.forward(332)
  counter.right(90)
  counter.hideturtle()
meowl.speed(0)
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


# Change color
def change_color_randomly(turtle_instance, color_list):
    new_color = rand.choice(color_list)
    turtle_instance.color(new_color)

# Change size
def change_size_randomly(turtle_instance, size_list):
    new_size = rand.choice(size_list)
    turtle_instance.shapesize(new_size)

# CODE TO ADD
# Add this function to your game code

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global meowl

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, meowl, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, meowl, score)

#-----events----------------
meowl.onclick(spot_clicked)
counter_setup()
scoreBox()
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor(bg_color)
wn.mainloop()