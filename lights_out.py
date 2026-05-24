import tkinter as tk
import random

from pyparsing import col

root = tk.Tk()
root.title('Lights Out')

ROWS = 5
COLS = 5

grid = [[0] * COLS for _ in range(ROWS)]

index = row * COLS + col
grid = [[0] * COLS for _ in range(ROWS)]

buttons = []

for r in range(ROWS):
    button_row = []
    for c in range(COLS):
        btn = tk.Button(root, width=4, height=2, command=lambda r=r, c=c: toggle(r, c))
        btn.grid(row=r, column=c)
        button_row.append(btn)
    buttons.append(button_row)

def toggle_cell(r, c):
    if 0 <= r < ROWS and 0 <= c < COLS:
        grid[r][c] = 1 - grid[r][c]
        if grid[r][c] == 1:
            colour = 'yellow'
        else:
            colour = 'grey20'
        buttons[r * COLS + c].config(bg=colour)
