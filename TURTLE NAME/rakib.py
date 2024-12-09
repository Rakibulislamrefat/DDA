import turtle
import time

def setup_screen():
    """Initialize and setup the screen"""
    screen = turtle.Screen()
    screen.title("RAKIB - Stylized Name")
    screen.bgcolor("#1a1a1a")  # Dark background
    screen.setup(800, 400)
    return screen

def create_turtle():
    """Create and configure the turtle"""
    t = turtle.Turtle()
    t.speed(6)
    t.pensize(10)
    t.color("#00ff9d")  # Neon green color
    return t

def move_to(t, x, y):
    """Move turtle to position without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)

def draw_r(t, x, y):
    """Draw letter R"""
    move_to(t, x, y)
    t.setheading(90)
    t.forward(120)  # Vertical line
    t.right(90)
    
    # Draw the curved part of R
    for _ in range(90):
        t.right(1)
        t.forward(0.7)
    
    # Draw diagonal leg
    t.setheading(-45)
    t.forward(80)

def draw_a(t, x, y):
    """Draw letter A"""
    move_to(t, x, y)
    
    # Left diagonal
    t.setheading(75)
    t.forward(130)
    
    # Right diagonal
    t.right(150)
    t.forward(130)
    
    # Cross line
    t.backward(65)
    t.right(105)
    t.forward(40)

def draw_k(t, x, y):
    """Draw letter K"""
    move_to(t, x, y)
    
    # Vertical line
    t.setheading(90)
    t.forward(120)
    t.backward(60)
    
    # Upper diagonal
    t.right(45)
    t.forward(80)
    t.backward(80)
    
    # Lower diagonal
    t.right(90)
    t.forward(80)

def draw_i(t, x, y):
    """Draw letter I"""
    move_to(t, x, y)
    t.setheading(90)
    t.forward(120)
    
    # Add dots for style
    t.penup()
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(130)
    t.dot(20)

def draw_b(t, x, y):
    """Draw letter B"""
    move_to(t, x, y)
    
    # Vertical line
    t.setheading(90)
    t.forward(120)
    
    # Upper loop
    t.right(90)
    for _ in range(180):
        t.right(1)
        t.forward(0.33)
    
    # Lower loop
    for _ in range(180):
        t.right(1)
        t.forward(0.33)

def add_decorations(t):
    """Add decorative elements"""
    original_color = t.color()[0]
    t.color("#ff3366")  # Pink color for decorations
    
    # Draw stars
    for star_pos in [(-250, 150), (250, 150), (-250, -150), (250, -150)]:
        move_to(t, star_pos[0], star_pos[1])
        for _ in range(5):
            t.forward(20)
            t.right(144)
    
    # Draw underline
    t.color(original_color)
    move_to(t, -300, -100)
    t.setheading(0)
    t.forward(600)

def main():
    screen = setup_screen()
    t = create_turtle()
    
    # Starting positions for each letter
    draw_r(t, -250, -50)
    draw_a(t, -150, -50)
    draw_k(t, -50, -50)
    draw_i(t, 50, -50)
    draw_b(t, 150, -50)
    
    # Add decorative elements
    add_decorations(t)
    
    # Hide turtle and display
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
