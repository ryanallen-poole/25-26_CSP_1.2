import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200 #location of ground
apple_letter_x_offset = -25 #horizontal offset
apple_letter_y_offset = -50
current_letter = "a"
screen_width =400
screen_height = 400

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


wn.bgpic("background.gif")
apple = trtl.Turtle()
wn.tracer(False)
apple.penup()

def reset_apple(active_apple):
    # Generate a random number - > pop that index
    # The letter we pop, becomes the letter on the apple
    global current_letter
    #how many letters left
    length_of_list = len(letters)
    #if we aren't out
    if(length_of_list != 0):
        index = rand.randint(0, length_of_list)
        current_letter = letters.pop(index)
        # Finish This First
        active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2),
                          rand.randint(-(screen_height) / 2, (screen_height) / 2))
        active_apple.goto(200,200)
        draw_apple(active_apple, current_letter)




# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, current_letter):
  active_apple.shape(apple_image)
  #draw_letter("A", active_apple)
  #Show Turtle Here
  active_apple.showturtle()
  draw_letter(current_letter, active_apple)
  wn.update()

def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)

def check_apple_a():
    if(current_letter == "a"):
        drop_apple()


draw_apple(apple,current_letter)

wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_b, "b")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_z, "z")


wn.onkeypress(drop_apple, "a")

wn.listen()