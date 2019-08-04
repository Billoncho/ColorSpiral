# ColorSpiral.py
# Billy Ridgeway
# Creates a spiral with a number of sides selected by the user.
# The user can select between 2 and 10 sides.

import turtle                       # Import turtle graphics.
t = turtle.Pen()                    # Creates a new turtle called t.
turtle.bgcolor("black")             # Set the background color to black.
t.speed(0)                          # Set the pen speed to fast.

# Ask the user to select a number of sides between 2 and 10.
sides = eval(input("Enter a number between 2 and 10: "))

# Create a list of colors to be used.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "light blue", "pink", "gray"]

for x in range (360):               # Set the variable 'x' to 360.
    t.pencolor(colors[x%sides])     # Cycle through the colors based upon the number of
                                    # sides chosen by the user.
    t.forward(x * 3 / sides + x)    # Move the pen forward by the value of 'x' times 3
                                    # divided by the number of sides plus the value of 'x'.
    t.left(360/sides + 1)           # Move the pen left by the value of 360 divided by
                                    # the number of sides plus 1.
    t.width(x*sides/200)            # Set the width of the pen to the value of 'x' times
                                    # the number of sides divided by 200.
    t.left(90)                      # Move the pen left 90 degrees.
