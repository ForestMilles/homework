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

"""2. Change the traffic light program so that changes occur automatically, driven by a timer."""
import turtle  # Tess becomes a traffic light.

wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
yay = turtle.Turtle()
bob = turtle.Turtle()
guest = turtle.Turtle()
hunt = turtle.Turtle()




def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

def draw_housing2():
    """ Draw a nice housing to hold the traffic lights """
    yay.pensize(3)
    yay.color("black", "darkgrey")
    yay.penup()
    yay.backward(180)
    yay.pendown()
    yay.begin_fill()
    yay.forward(80)
    yay.left(90)
    yay.forward(275)
    yay.circle(40, 180)
    yay.forward(275)
    yay.left(90)
    yay.end_fill()


draw_housing()
draw_housing2()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
yay.penup()
yay.forward(40)
yay.left(90)
yay.forward(50)
yay.shape("circle")
yay.shapesize(3)
yay.fillcolor("gray")

bob.penup()
bob.goto(yay.position()[0], (yay.position()[1] + 75))
bob.shape('circle')
bob.shapesize(3)
bob.fillcolor("gray")

guest.penup()
guest.goto(bob.position()[0], (bob.position()[1] + 75))
guest.shape('circle')
guest.shapesize(3)
guest.fillcolor('gray')

hunt.penup()
hunt.goto(guest.position()[0], (guest.position()[1] + 75))
hunt.shape('circle')
hunt.shapesize(3)
hunt.fillcolor('gray')

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0
state_num_1 = 0


def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:  # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    wn.ontimer(advance_state_machine, "5000")


def advance_state_machine2():
    global state_num_1
    if state_num_1 == 0:  # Transition from state 0 to state 1
        guest.fillcolor('gray')
        yay.fillcolor('green')
        state_num_1 = 1
    elif state_num_1 == 1:  # Transition from state 1 to state 2
        yay.fillcolor('gray')
        bob.fillcolor('green')
        hunt.fillcolor('orange')
        state_num_1 = 2
    elif state_num_1 == 2:
        bob.fillcolor('gray')
        hunt.fillcolor('gray')
        guest.fillcolor('red')
        state_num_1 = 0
    wn.ontimer(advance_state_machine2, "10000")


advance_state_machine()
advance_state_machine2()

wn.mainloop()