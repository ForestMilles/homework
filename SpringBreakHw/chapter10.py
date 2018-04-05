"""1. Add some new key bindings to the first sample program:

Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays between 1 and 20 (inclusive).
Handle some other keys to change some attributes of tess, or attributes of the window, or to give her new behaviour that can be controlled from the keyboard."""

import turtle

turtle.setup(400, 500)  # Determine the window size
wn = turtle.Screen()  # Get a reference to the window
wn.title("Handling keypresses!")  # Change the window title
wn.bgcolor("lightgreen")  # Set the background color
tess = turtle.Turtle()  # Create our favorite turtle
tess_size = 3
tess_size = tess.pensize(tess_size)


# The next four functions are our "event handlers".
def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)

def h4():
    wn.bye()


def red():
    tess.color("red")


def green():
    tess.color('green')


def blue():
    tess.color('blue')

sz = 1

def h8():
    global sz
    sz +=  1
    if sz > 20:
        sz = 20
    tess.pensize(sz)

def h9():
    global sz
    sz -= 1
    if sz<1:
        sz=1

def h10():
    tess.circle(20)

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(red, "r")
wn.onkey(green, "g")
wn.onkey(blue, "b")
wn.onkey(h8, "=")
wn.onkey(h9, "-")
wn.onkey(h10, "c")

wn.listen()
wn.mainloop()

