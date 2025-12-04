import tkinter as tk
from tkinter import messagebox
import random
import string

list_words = ["float", "airbag", "sweater", "table", "cap"]
MAX_LIVES = 6

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("400x300")
        
        self.word_to_guess = ""
        self.guessed_letters = set()
        self.lives_remaining = MAX_LIVES
        
        self.setup_widgets()
        self.start_new_game()

    def setup_widgets(self):
        # Label for displaying the current word status (e.g., "_ _ _")
        self.word_display = tk.Label(self.master, text="", font=("Helvetica", 24))
        self.word_display.pack(pady=20)
        
        # Label for messages (win/lose/guessed letters)
        self.message_label = tk.Label(self.master, text=f"Lives: {self.lives_remaining}", font=("Helvetica", 12))
        self.message_label.pack(pady=10)
        
        # Entry widget for the user to type a guess
        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 16), width=5)
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", self.process_guess_event) # Allows pressing Enter key
        
        # Button to submit the guess
        self.submit_button = tk.Button(self.master, text="Guess Letter", command=self.process_guess_event)
        self.submit_button.pack(pady=10)

        # Button to start a new game
        self.new_game_button = tk.Button(self.master, text="New Game", command=self.start_new_game)
        self.new_game_button.pack(pady=10)
        self.new_game_button.config(state=tk.DISABLED) # Disable until game ends

    def start_new_game(self):
        self.word_to_guess = random.choice(list_words).lower()
        self.guessed_letters = set()
        self.lives_remaining = MAX_LIVES
        self.update_display()
        self.message_label.config(text=f"Lives: {self.lives_remaining}")
        self.guess_entry.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.NORMAL)
        self.new_game_button.config(state=tk.DISABLED)
        self.guess_entry.focus_set() # Set focus to the entry box

    def update_display(self):
        # Update the word display with underscores and correct letters
        display_text = ' '.join([
            char if char in self.guessed_letters else '_' for char in self.word_to_guess
        ])
        self.word_display.config(text=display_text)
        
    def process_guess_event(self, event=None):
        guess = self.guess_entry.get().strip().lower()
        self.guess_entry.delete(0, tk.END) # Clear the entry box

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            messagebox.showwarning("Invalid Input", "Please enter a single valid letter.")
            return

        if guess in self.guessed_letters:
            self.message_label.config(text=f"You already guessed '{guess}'. Lives: {self.lives_remaining}")
            return
        
        self.guessed_letters.add(guess)

        if guess in self.word_to_guess:
            self.update_display()
            if '_' not in self.word_display.cget("text"):
                self.game_over(True)
        else:
            self.lives_remaining -= 1
            self.message_label.config(text=f"'{guess}' is incorrect. Lives: {self.lives_remaining}")
            if self.lives_remaining <= 0:
                self.game_over(False)
        
    def game_over(self, won):
        self.guess_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.new_game_button.config(state=tk.NORMAL)
        
        if won:
            messagebox.showinfo("Game Over", "Congratulations! You won!")
        else:
            messagebox.showinfo("Game Over", f"You lost! The word was '{self.word_to_guess}'.")

# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    game_gui = HangmanGUI(root)
    root.mainloop() # Start the Tkinter event loop
