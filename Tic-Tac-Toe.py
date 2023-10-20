import tkinter as tk
from tkinter import messagebox
import random

# Initialize the Tic-Tac-Toe board
board = [' ' for _ in range(9)]
player = 'X'
ai = 'O'

def check_win(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def make_move(position):
    global player
    if board[position] == ' ' and not check_win(player) and not check_win(ai):
        board[position] = player
        buttons[position]['text'] = player
        if check_win(player):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
        elif ' ' not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        else:
            ai_move()
            if check_win(ai):
                messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
            elif ' ' not in board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")

def ai_move():
    empty_cells = [i for i, val in enumerate(board) if val == ' ']
    if empty_cells:
        ai_position = random.choice(empty_cells)
        board[ai_position] = ai
        buttons[ai_position]['text'] = ai

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create and configure buttons
buttons = [None] * 9
for i in range(9):
    row, col = divmod(i, 3)
    buttons[i] = tk.Button(root, text=' ', width=10, height=3, command=lambda i=i: make_move(i))
    buttons[i].grid(row=row, column=col)

# Run the main loop
root.mainloop()
