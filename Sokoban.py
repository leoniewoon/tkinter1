level1 = [
    "##########",
    "#        #",
    "#   .$.  #",
    "#   .@.  #",
    "#        #",
    "##########"
]

level2 = [
    "############",
    "#     #    #",
    "# $     $  #",
    "#    @     #",
    "#  .  #  . #",
    "############"
]

level3 = [
    "#########",
    "#       #",
    "# $.$   #",
    "#  @..  #",
    "##########"
]

LEVELS = [level1, level2, level3]

import tkinter as tk
TILE = 100

root = tk.Tk()
root.title("Sokoban")



images = {
    'wall': tk.PhotoImage(file='my_game/maps/tiles/wall.png'),
    'floor': tk.PhotoImage(file='my_game/maps/tiles/floor.png'),
    'player': tk.PhotoImage(file='my_game/maps/tiles/player.png'),
    'goal': tk.PhotoImage(file='my_game/maps/tiles/goal.png'),
    'box': tk.PhotoImage(file='my_game/maps/tiles/box.png')
}

game_map = []
player_r = 0
player_c = 0

def load_level(index):
    global game_map, player_r, player_c

    game_map = []
    for row_string in LEVELS[index]:
        game_map.append(list(row_string))

    for r in range(len(game_map)):
        for c in range(len(game_map[r])):
            if game_map[r][c] in ("@", "+"):
                player_r = r 
                player_c = c

    rows = len(game_map)
    cols = len(game_map[0])
    canvas.config(width=cols * TILE, height=rows * TILE)

TILE_IMAGE = {
    '#': 'wall',
    ' ': 'floor',
    '.': 'goal',
    '+': 'player_goal',
    '@': 'player',
    '$': 'box',
    '*': 'box_goal',
}

def draw_tile(r, c, key):
    x = c * TILE
    y = r * TILE
    canvas.create_image(x, y, image=images[key], anchor='nw')

def draw_world():
    canvas.delete("all")
    for r in range(len(game_map)):
        for c in range(len(game_map[r])):
            ch = game_map[r][c]
            key = TILE_IMAGE[ch]
            draw_tile(r, c, key)

def try_move(dr, dc):
    global player_r, player_c

    nr = player_r + dr
    nc = player_c + dc

    if 0 <= nr < len(game_map) and 0 <= nc < len(game_map[0]):
        return
    tile = game_map[nr][nc]

    if tile == '#':
        return  
    if tile in (' ', '.'):
        _move_player(nr, nc)
    elif tile in ('$', '*'):
        br = nr + dr
        bc = nc + dc

        if not (0 <= br < len(game_map) and 0 <= bc < len(game_map[0])):
            return
        box_dest = game_map

        if box_dest[br][bc] in (' ', '.'):
            _push_box(nr, nc, br, bc)
            _move_player(nr, nc)

    check_win()
    draw_world()

def _move_player(nr, nc):
    global player_r, player_c

    if game_map[player_r][player_c] == '+':
        game_map[player_r][player_c] = '.'
    else:
        game_map[player_r][player_c] = ' '

    if game_map[nr][nc] == '.':
        game_map[nr][nc] = '+'
    else:
        game_map[nr][nc] = '@'

    player_r, player_c = nr, nc

def _push_box(br, bc, nr, nc):

    if game_map[dest_r][dest_c] == '.':
        game_map[dest_r][dest_c] = '*'
    else:
        game_map[dest_r][dest_c] = '$'

    if game_map[br][bc] == '*':
        game_map[br][bc] = '.'
    else:
        game_map[br][bc] = ' '

def check_win():
    global current_level
    for row in game_map:
        if '$' in row:
            return

    current_level += 1
    if current_level < len(LEVELS):
        load_level(current_level)
        draw_world()

    else:
        canvas.delete("all")
        canvas.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2,
                           text="You Win!", font=("Arial", 18, 'bold'), fill="green")


def on_key(event):
    if event.keysym == "Up":
        try_move(-1, 0)
    elif event.keysym == "Down":
        try_move(1, 0)
    elif event.keysym == "Left":
        try_move(0, -1)
    elif event.keysym == "Right":
        try_move(0, 1)
    elif event.keysym == "r":
        load_level(current_level)
        draw_world()
root.bind("<Key>", on_key)

canvas = tk.Canvas(root, width=TILE, height=TILE)
canvas.pack()

load_level(0)
draw_world()

root.mainloop()
