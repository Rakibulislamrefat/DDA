import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Rock Paper Scissors")
screen.bgcolor("#2C3E50")
screen.setup(800, 600)

# Create score variables
player_score = 0
computer_score = 0

# Create and position the writer turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.color("white")
writer.penup()

# Create choice turtle
choice_display = turtle.Turtle()
choice_display.hideturtle()
choice_display.color("white")
choice_display.penup()

def draw_centered_text(turtle_obj, text, y_pos, font_size=20):
    """Helper function to draw centered text"""
    turtle_obj.clear()
    turtle_obj.goto(0, y_pos)
    turtle_obj.write(text, align="center", font=("Arial", font_size, "bold"))

def update_score():
    """Update the score display"""
    score_text = f"Player: {player_score}  Computer: {computer_score}"
    draw_centered_text(writer, score_text, 220)

def display_choices(player_choice, computer_choice, result):
    """Display the choices and result"""
    choice_text = f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n\n{result}"
    draw_centered_text(choice_display, choice_text, 0)

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game"""
    global player_score, computer_score
    
    if player_choice == computer_choice:
        return "It's a tie!"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combinations[player_choice] == computer_choice:
        player_score += 1
        return "You win! 🎉"
    else:
        computer_score += 1
        return "Computer wins! 💻"

def create_button(x, y, text):
    """Create a clickable button"""
    button = turtle.Turtle()
    button.hideturtle()
    button.penup()
    button.goto(x, y)
    
    # Draw button background
    button.color("white")
    button.begin_fill()
    for _ in range(2):
        button.forward(100)
        button.left(90)
        button.forward(40)
        button.left(90)
    button.end_fill()
    
    # Write button text
    button.color("black")
    button.goto(x + 50, y + 10)
    button.write(text, align="center", font=("Arial", 12, "bold"))

def handle_click(x, y):
    """Handle mouse clicks"""
    choices = ["rock", "paper", "scissors"]
    
    # Check which button was clicked
    if -150 <= x <= -50 and -100 <= y <= -60:
        player_choice = "rock"
    elif -50 <= x <= 50 and -100 <= y <= -60:
        player_choice = "paper"
    elif 50 <= x <= 150 and -100 <= y <= -60:
        player_choice = "scissors"
    else:
        return

    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    display_choices(player_choice, computer_choice, result)
    update_score()

def setup_game():
    """Initialize the game"""
    # Clear any existing drawings
    screen.clear()
    screen.bgcolor("#2C3E50")
    
    # Draw title
    draw_centered_text(writer, "Rock Paper Scissors", 150, 30)
    
    # Create buttons
    create_button(-150, -100, "Rock")
    create_button(-50, -100, "Paper")
    create_button(50, -100, "Scissors")
    
    # Draw initial score
    update_score()
    
    # Draw instructions
    draw_centered_text(choice_display, "Click a button to play!", 0)
    
    # Set up click handling
    screen.onclick(handle_click)

# Start the game
setup_game()

# Keep the window open
screen.mainloop()
