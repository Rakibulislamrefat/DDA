import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("RAKIB")

# Create and customize the turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(5)
t.color("blue")

# Function to move without drawing
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Starting position
move_to(-200, 0)

# Draw R
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(70)

# Move to position for A
move_to(-120, 0)
t.left(45)
t.forward(100)
t.right(150)
t.forward(100)
t.backward(50)
t.right(105)
t.forward(35)

# Move to position for K
move_to(-40, 0)
t.left(75)
t.forward(100)
t.backward(50)
t.right(45)
t.forward(60)
t.backward(60)
t.right(90)
t.forward(60)

# Move to position for I
move_to(40, 0)
t.left(135)
t.forward(100)

# Move to position for B
move_to(100, 0)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(45)
t.right(90)
t.forward(50)
t.backward(50)
t.left(90)
t.forward(45)
t.right(90)
t.forward(50)

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop()
