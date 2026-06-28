level1 = [
    "#######",
    "#     #",
    "# .$. #",
    "# .@. #",
    "#     #",
    "#######"
]

level2 = [
    "#########",
    "#   #   #",
    "# $   $ #",
    "#   @   #",
    "# . # . #",
    "#########"
]

level3 = [
    "########",
    "#      #",
    "# $  $ #",
    "# @..  #",
    "########"
]

LEVELS = [level1, level2, level3]

import tkinter as tk
TILE = 64

current_level = 0

root = tk.Tk()
root.title("Sokoban")

images = {
    'wall': tk.PhotoImage(file='tiles/wall.png'),
    'floor': tk.PhotoImage(file='tiles/floor.png'),
    'box': tk.PhotoImage(file='tiles/box.png'),
    'goal': tk.PhotoImage(file='tiles/goal.png'),
    'player': tk.PhotoImage(file='tiles/player.png')
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
            if game_map[r][c] == ('@', '+'):
                player_r, player_c = r, c
    
    rows = len(game_map)
    cols = len(game_map[0])
    canvas.config(width=cols*TILE, height=rows*TILE)

TILE_IMAGE = {
    '#': 'wall', 
    ' ': 'floor',
    '$': 'box',
    '.': 'goal',
    '@': 'player',
    '+': 'player_goal'
}