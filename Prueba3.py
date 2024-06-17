import turtle
import qrcode


wn = turtle.Screen()
wn.title("Para mi alea bella")
wn.bgcolor("white")


heart_turtle = turtle.Turtle()
heart_turtle.pensize(2)
heart_turtle.speed(1)


def draw_half_heart():
    heart_turtle.begin_fill()  #
    heart_turtle.left(50)      #
    heart_turtle.forward(67)   #
    heart_turtle.circle(25, 200)#
    heart_turtle.end_fill()    #


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



heart_turtle.color("red")
draw_half_heart()


heart_turtle.penup()
heart_turtle.goto(0, 0)
heart_turtle.setheading(0)
heart_turtle.pendown()


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


heart_turtle.penup()
heart_turtle.goto(-190, -80)
heart_turtle.pendown()
heart_turtle.color("black")
heart_turtle.write("Te amo muchisimo alea preciosa\n Te adoro con todo mi corazón", font=("Arial", 16, "bold"))


heart_turtle.hideturtle()
wn.mainloop()



img = qrcode.make('https://youtu.be/nK0c-bh0UV0')
type(img) 
img.save("some_file.png")
