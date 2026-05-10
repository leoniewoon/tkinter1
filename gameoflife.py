import tkinter as tk
import random

ROWS = 20
COLS = 20
CELL_SIZE = 30

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

root = tk.Tk()
root.title("Game of Life")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

board = []
for r in range(ROWS):
    row = []
    for c in range(COLS):
        row.append(0)
    board.append(row)

def draw_cell(r, c):
    x1 = c * CELL_SIZE
    y1 = r * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE

    color = "black" if board[r][c] == 1 else "white"

    canvas.create_rectangle(x1, y1, x2, y2,
                            fill=color, outline="gray")
    
def draw_board():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            draw_cell(r, c)

def toggle_cell(event):
    c = event.x // CELL_SIZE
    r = event.y // CELL_SIZE

    if 0 <= r < ROWS and 0 <= c < COLS:
        if board[r][c] == 0:
            board[r][c] = 1
        else:
            board[r][c] = 0
        draw_board()

canvas.bind("<Button-1>", toggle_cell)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

def clear_board():
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c] = 0
    draw_board()

def random_board():
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c] = random.randint(0,1)
    draw_board()

def count_neighbors(r,c):
    count = 0

    for dr in (-1, 0, 1): 
        for dc in (-1, 0, 1):

            if dr == 1 and dc == 1:
                continue
            
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < 1 and 0<= nc < 1:
                if board[nr][nc]==1:
                    count += 1

    return count

clear_btn = tk.Button(button_frame, text="Clear", command=clear_board)
clear_btn.grid(row=0, column=0, padx=5)

rand_btn = tk.Button(button_frame, text="Random", command=random_board)
rand_btn.grid(row=0, column=1, padx=5)

draw_board()
root.mainloop()