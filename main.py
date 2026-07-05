MAP = [
    "##########",
    "##.....#.#",
    "#..##.#..#",
    "#.##..P..#",
    "#..##..#.#",
    "##....#..#",
    "##########"
]

import tkinter as tk
TILE = 48
ROWS = len(MAP)
COLS = len(MAP[0])

WIDTH = COLS * TILE
HEIGHT = ROWS * TILE

root = tk.Tk()
root.title("Map Walker")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

player_r = 0
player_c = 0

for r in range(ROWS):
    for c in range(COLS):
        if MAP[r][c] == "P":
            player_r, player_c = r, c

images = {
    'wall': tk.PhotoImage(file='my_game/maps/tiles/wall.png'),
    'floor': tk.PhotoImage(file='my_game/maps/tiles/floor.png'),
    'player': tk.PhotoImage(file='my_game/maps/tiles/player.png'),
    'goal': tk.PhotoImage(file='my_game/maps/tiles/goal.png'),
    'box': tk.PhotoImage(file='my_game/maps/tiles/box.png')
}

def load_map(maps):
    with open(maps, 'r') as f:
        lines = f.readlines()

    #TODO: remove \n from each line 
    lines = [line.strip() for line in lines]

    if len(lines) == 0:
        raise ValueError('Map is empty')

    width = len(lines[0])
    for line in lines:
        if len(line) != width:
            raise ValueError('Map is not rectangular')
    
    allowed = set('#.P')
    p_count = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
             ch = lines[r][c]
        if ch not in allowed:
            raise ValueError(f"Invalid character '{ch}' at ({r}, {c})")
        if ch == 'P':
            p_count += 1
    if p_count != 1:
        raise ValueError('Map must contain exactly one player')
    return lines

def draw_wall(r, c):
    x1 = c * TILE
    y1 = r * TILE
    x2 = x1 + TILE
    y2 = y1 + TILE
    canvas.create_image(x1, y1, anchor="nw", image=images['wall'])

def draw_tile(r, c, ch):
    x1 = c * TILE
    y1 = r * TILE
    x2 = x1 + TILE
    y2 = y1 + TILE
    if ch == "#":
        color = "gray"
    else:
        color = "white"
    canvas.create_image(x1, y1, anchor="nw", image=images['floor'])

def draw_player(r, c):
    x1 = c * TILE
    y1 = r * TILE
    x2 = x1 + TILE
    y2 = y1 + TILE
    canvas.create_image(x1, y1, anchor="nw", image=images['player'])

def draw_world():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            if MAP[r][c] == "#":
                draw_wall(r, c)
            else:
                draw_tile(r, c, MAP[r][c])
    draw_player(player_r, player_c)
draw_world()

def try_move(dr, dc):
    global player_r, player_c
    nr = player_r + dr
    nc = player_c + dc

    #bounds safety
    if not (0 <= nr < ROWS and 0 <= nc < COLS):
        return
    
    #collision
    if MAP[nr][nc] == "#":
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
root.mainloop()