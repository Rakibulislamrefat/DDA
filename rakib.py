import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("RAKIB")
screen.setup(800, 400)  # Set window size

# Create and customize the turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(8)
t.color("#1E88E5")  # Nice blue color

# Function to move without drawing
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)  # Reset heading to 0

# Starting position
move_to(-300, -50)

# Draw R
t.setheading(90)
t.forward(150)  # Vertical line
t.right(90)
t.forward(60)  # Top horizontal
t.right(90)
t.forward(60)  # Middle part
t.right(90)
t.forward(60)
t.setheading(-45)  # Diagonal leg
t.forward(100)

# Draw A
move_to(-180, -50)
t.setheading(75)
t.forward(155)  # Left diagonal
t.right(150)
t.forward(155)  # Right diagonal
t.backward(77)  # Go back to middle
t.right(105)
t.forward(50)  # Cross line

# Draw K
move_to(-80, -50)
t.setheading(90)
t.forward(150)  # Vertical line
t.backward(75)  # Back to middle
t.right(45)
t.forward(85)  # Upper diagonal
t.backward(85)  # Back to middle
t.right(90)
t.forward(85)  # Lower diagonal

# Draw I
move_to(20, -50)
t.setheading(90)
t.forward(150)  # Vertical line

# Draw B
move_to(80, -50)
t.setheading(90)
t.forward(150)  # Vertical line
t.right(90)
t.forward(60)  # Top horizontal
for _ in range(180):  # Top curve
    t.right(1)
    t.forward(0.52)
t.forward(60)  # Middle horizontal
for _ in range(180):  # Bottom curve
    t.right(1)
    t.forward(0.52)
t.forward(60)  # Bottom horizontal

# Add a simple underline
move_to(-320, -70)
t.setheading(0)
t.forward(480)

# Hide turtle and display
t.hideturtle()
screen.mainloop()
