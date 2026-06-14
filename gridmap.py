import tkinter as tk
from PIL import Image, ImageTk

def load_map(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    if len(lines) == 0:
        raise ValueError("Map file is empty")
    
    width = len(lines[0])
    for line in lines:
        if len(line) != width:
            raise ValueError("Map is not rectangular")
        
    allowed = set("#.PE")
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

orginal_images = {
    'floor': Image.open("tiles/ground.png"), 
    'wall': Image.open("tiles/wall.png"),
    'player': Image.open("tiles/player.png"),
    'exit': Image.open("tiles/exit.png"),
}

resized_images = {
    'floor': ImageTk.PhotoImage(orginal_images['floor'].resize((TILE, TILE))),
    'wall': ImageTk.PhotoImage(orginal_images['wall'].resize((TILE, TILE))),
    'player': ImageTk.PhotoImage(orginal_images['player'].resize((TILE, TILE))),
    'exit': ImageTk.PhotoImage(orginal_images['exit'].resize((TILE, TILE))),
}

tile_lookup = {
    '#': 'wall',
    '.': 'floor',
    'P': 'player',
    'E': 'exit'
}   

for r in range(ROWS):
    for c in range(COLS):
        if MAP [r][c] == 'P':
            player_r = r
            player_c = c

def draw_image_tile(r, c, key):
    x = c * TILE
    y = r * TILE
    canvas.create_image(x, y, image=resized_images[key], anchor="nw")   

def draw_tile(r, c, ch):
    x1 = c * TILE
    y1 = r * TILE
    x2 = x1 + TILE
    y2 = y1 + TILE

    if ch == '#':
        color = "gray"
    else:
        color = "white"

    canvas.create_image(x1, y1, image=resized_images[tile_lookup[ch]], anchor="nw")

def draw_player(r, c):
    x1 = c * TILE
    y1 = r * TILE
    x2 = x1 + TILE
    y2 = y1 + TILE
    canvas.create_image(x1, y1, image=resized_images['player'], anchor="nw")

def draw_world():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            ch = MAP[r][c]
            draw_tile(r, c, ch)

    draw_image_tile(player_r, player_c, 'player')

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
    #MAP[dr][dc] = '.'
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