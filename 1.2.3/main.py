#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
drawer = trtl.Turtle()


def drop_apple():
    apple.goto(100,-200)

def draw_letter(letter, active_apple):...

draw_apple(apple)
wn.onkeypress()
# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.


#-----function calls-----
wn.onkeypress(draw_an_A, "a")

wn.listen()

draw_apple(apple)

wn.mainloop()