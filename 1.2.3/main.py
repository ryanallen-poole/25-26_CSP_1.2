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
        #active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2),
                          #rand.randint(-(screen_height) / 2, (screen_height) / 2))
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
def check_apple_b():
    if(current_letter == "b"):
        drop_apple()
def check_apple_c():
    if(current_letter == "c"):
        drop_apple()
def check_apple_d():
    if(current_letter == "d"):
        drop_apple()
def check_apple_e():
    if(current_letter == "e"):
        drop_apple()
def check_apple_f():
    if(current_letter == "f"):
        drop_apple()
def check_apple_g():
    if(current_letter == "g"):
        drop_apple()
def check_apple_h():
    if(current_letter == "h"):
        drop_apple()
def check_apple_i():
    if(current_letter == "i"):
        drop_apple()
def check_apple_j():
    if(current_letter == "j"):
        drop_apple()
def check_apple_k():
    if(current_letter == "k"):
        drop_apple()
def check_apple_l():
    if(current_letter == "l"):
        drop_apple()
def check_apple_m():
    if(current_letter == "m"):
        drop_apple()
def check_apple_n():
    if(current_letter == "n"):
        drop_apple()
def check_apple_o():
    if(current_letter == "o"):
        drop_apple()
def check_apple_p():
    if(current_letter == "p"):
        drop_apple()
def check_apple_q():
    if(current_letter == "q"):
        drop_apple()
def check_apple_r():
    if(current_letter == "r"):
        drop_apple()
def check_apple_s():
    if(current_letter == "s"):
        drop_apple()
def check_apple_t():
    if(current_letter == "t"):
        drop_apple()
def check_apple_u():
    if(current_letter == "u"):
        drop_apple()
def check_apple_v():
    if(current_letter == "v"):
        drop_apple()
def check_apple_w():
    if(current_letter == "w"):
        drop_apple()
def check_apple_x():
    if(current_letter == "x"):
        drop_apple()
def check_apple_y():
    if(current_letter == "y"):
        drop_apple()
def check_apple_z():
    if(current_letter == "z"):
        drop_apple()

draw_apple(apple,current_letter)

wn.onkey(check_apple_a, "a")
wn.onkey(check_apple_b, "b")
wn.onkey(check_apple_c, "c")
wn.onkey(check_apple_d, "d")
wn.onkey(check_apple_e, "e")
wn.onkey(check_apple_f, "f")
wn.onkey(check_apple_g, "g")
wn.onkey(check_apple_h, "h")
wn.onkey(check_apple_i, "i")
wn.onkey(check_apple_j, "j")
wn.onkey(check_apple_k, "k")
wn.onkey(check_apple_l, "l")
wn.onkey(check_apple_m, "m")
wn.onkey(check_apple_n, "n")
wn.onkey(check_apple_o, "o")
wn.onkey(check_apple_p, "p")
wn.onkey(check_apple_q, "q")
wn.onkey(check_apple_r, "r")
wn.onkey(check_apple_s, "s")
wn.onkey(check_apple_t, "t")
wn.onkey(check_apple_u, "u")
wn.onkey(check_apple_v, "v")
wn.onkey(check_apple_w, "w")
wn.onkey(check_apple_x, "x")
wn.onkey(check_apple_y, "y")
wn.onkey(check_apple_z, "z")



wn.listen()
trtl.mainloop()