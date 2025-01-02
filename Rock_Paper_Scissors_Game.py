import random
import tkinter as tk
from tkinter import messagebox

# Initialize global variables for scores
user_score = 0
computer_score = 0
high_score = 0  # Track the highest score

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score, high_score

    # Random computer choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    # Determine the outcome
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Update the result and score labels
    result_label.config(
        text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}"
    )
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}\nHigh Score: {high_score}")
    
    # Disable buttons after the game result
    disable_buttons()

    # Update high score if necessary
    if user_score > high_score:
        high_score = user_score

# Function to restart the game
def play_again():
    global user_score, computer_score
    result_label.config(text="Make your choice to play!")
    # Update the score label to include the high score
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}\nHigh Score: {high_score}")
    enable_buttons()  # Enable buttons after restarting

# Disable buttons
def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

# Enable buttons
def enable_buttons():
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

# Set up the main application window
app = tk.Tk()
app.title("Rock, Paper, Scissors Game")
app.geometry("400x400")
app.config(bg="lightblue")  # Set a background color

header_label = tk.Label(app, text="Rock, Paper, Scissors", font=("Helvetica", 16, "bold"), bg="lightblue")
header_label.pack(pady=10)

result_label = tk.Label(app, text="Make your choice to play!", font=("Arial", 12), wraplength=350, bg="lightblue")
result_label.pack(pady=20)

button_frame = tk.Frame(app, bg="lightblue")  # Frame background color
button_frame.pack(pady=10)

# Buttons for each choice (Rock, Paper, Scissors)
rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), bg="lightgreen", command=lambda: determine_winner("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), bg="lightcoral", command=lambda: determine_winner("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), bg="lightyellow", command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Display score label and play again button
score_label = tk.Label(app, text=f"Score - You: {user_score}, Computer: {computer_score}", font=("Arial", 12), bg="lightblue")
score_label.pack(pady=10)

play_again_button = tk.Button(app, text="Play Again", font=("Arial", 12), command=play_again, bg="lightgreen")
play_again_button.pack(pady=10)

exit_button = tk.Button(app, text="Exit", font=("Arial", 12), command=app.quit, bg="lightcoral")
exit_button.pack(pady=10)

# Run the application
app.mainloop()
