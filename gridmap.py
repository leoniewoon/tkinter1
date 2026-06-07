# MAP = [
#     "##########",
#     "#........#",
#     "#..##....#",
#     "#..#..P..#",
#     "#..##....#",
#     "#........#",
#     "##########"
# ]
def load_map(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    if len(lines) == 0:
        raise ValueError("Map file is empty")
    
    width = len(lines[0])
    for line in lines:
        if len(line) != width:
            raise ValueError("Map is not rectangular")
        
    allowed = set("#.P")
    p_count = 0

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            ch = lines[r][c]
            if ch not in allowed:
                raise ValueError(f"Invalid character '{ch}' at ({r}, {c})")
            if ch == 'P':
                p_count += 1

    if p_count != 1:
        raise ValueError(f"Map must contain exactly one player")

    return lines

MAP = load_map("maps/map1.txt")

import tkinter as tk

TILE = 48
ROWS = len(MAP)
COLS = len(MAP[0])

W = COLS * TILE
H = ROWS * TILE

root = tk.Tk()
root.title("Map Walker")
canvas = tk.Canvas(root, width=W, height=H)
canvas.pack()

player_r = 0
player_c = 0

for r in range(ROWS):
    for c in range(COLS):
        if MAP [r][c] == 'P':
            player_r = r
            player_c = c

def draw_tile(r, c, ch):
    x1 = c * TILE
    y1 = r * TILE
    x2 = x1 + TILE
    y2 = y1 + TILE

    if ch == '#':
        color = "gray"
    else:
        color = "white"

    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

def draw_player(r, c):
    x1 = c * TILE
    y1 = r * TILE
    x2 = x1 + TILE
    y2 = y1 + TILE
    canvas.create_oval(x1+8, y1+8, x2-8, y2-8, fill="orange", outline="black")

def draw_world():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            draw_tile(r, c, MAP[r][c])
    draw_player(player_r, player_c)

def try_move(dr, dc):
    global player_r, player_c

    nr = player_r + dr
    nc = player_c + dc

    if not (0 <= nr < ROWS and 0 <= nc < COLS):
        return
    
    if MAP[nr][nc] == '#':
        return
    
    player_r = nr
    player_c = nc

    draw_world()

def on_key(event):
    if event.keysym == "Up":
        try_move(-1, 0)
    elif event.keysym == "Down":
        try_move(1, 0)
    elif event.keysym == "Left":
        try_move(0, -1)
    elif event.keysym == "Right":
        try_move(0, 1)

root.bind("<Key>", on_key)

draw_world()
root.mainloop()