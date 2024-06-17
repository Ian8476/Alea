import qrcode

import turtle
import qrcode

# Setup the screen
wn = turtle.Screen()
wn.title("Heart Drawing with Turtle")
wn.bgcolor("white")

# Create a turtle object
heart_turtle = turtle.Turtle()
heart_turtle.pensize(2)
heart_turtle.speed(1)

# Function to draw half of a heart shape
def draw_half_heart():
    heart_turtle.begin_fill()  #
    heart_turtle.left(50)      #
    heart_turtle.forward(67)   #
    heart_turtle.circle(25, 200)#
    heart_turtle.end_fill()    #

# Function to draw an arrow
def draw_arrow(x, y, angle):
    heart_turtle.penup()
    heart_turtle.goto(x, y)
    heart_turtle.pendown()
    heart_turtle.setheading(angle)
    heart_turtle.forward(150)
    heart_turtle.right(135)
    heart_turtle.forward(10)
    heart_turtle.backward(10)
    heart_turtle.left(90)
    heart_turtle.forward(10)
    heart_turtle.backward(10)


# Draw the first half of the heart
heart_turtle.color("red")
draw_half_heart()

# Draw the first arrow


# Reposition turtle for the second half of the heart
heart_turtle.penup()
heart_turtle.goto(0, 0)
heart_turtle.setheading(0)
heart_turtle.pendown()

# Draw the second half of the heart
heart_turtle.color("red")
heart_turtle.begin_fill()
#heart_turtle.left(50)
#heart_turtle.forward(67)
#heart_turtle.circle(25, 200)
heart_turtle.left(90)
heart_turtle.forward(67)
heart_turtle.circle(25, 200)
heart_turtle.left(20)
heart_turtle.forward(76)
heart_turtle.end_fill()

# Draw the second arrow

# Write text
heart_turtle.penup()
heart_turtle.goto(-190, -80)
heart_turtle.pendown()
heart_turtle.color("black")
heart_turtle.write("Te amo muchisimo alea preciosa\n Te adoro con todo mi corazón", font=("Arial", 16, "bold"))

# Hide the turtle and display the window
heart_turtle.hideturtle()
wn.mainloop()



img = qrcode.make('https://youtu.be/nK0c-bh0UV0')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")