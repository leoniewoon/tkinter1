import tkinter as tk
import random

root = tk.Tk()
root.title("Snake -1")

SIZE = 20
W = 600
H = 600

max_x = 30
max_y = 30

canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()

score = 0
score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack() 

snake = [(10, 10)]

dx = 1
dy = 0

food = (random.randint(0, W//SIZE - 1),
        random.randint(0, H//SIZE - 1))

def draw():
    canvas.delete("all")
    canvas.create_text(60, 10,
                       text=f"Score: {score}",
                       fill="black",
                       font=("Arial", 14))
    fx, fy = food
    canvas.create_rectangle(fx*SIZE, fy*SIZE, 
                           (fx+1)*SIZE, (fy+1)*SIZE, 
                           fill="red")

    for x, y in snake:
        canvas.create_rectangle(x*SIZE, y*SIZE,
                               (x+1)*SIZE, (y+1)*SIZE, 
                               fill="green")
        
def game_loop():
    global snake, food, score

    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)


    if new_head[0] < 0 or new_head[0] >= max_x or \
       new_head[1] < 0 or new_head[1] >= max_y:
        print("Game Over!")
        return 

    if new_head in snake:
        print("Game Over!")
        return

    snake.insert(0, new_head)
    
    if new_head == food:
        score_label.config(text=f"Score: {score}")
        print("Score:", score)
        food = (random.randint(0, W//SIZE - 1),
                random.randint(0, H//SIZE - 1))
    else:
        snake.pop()

    draw()
    root.after(100, game_loop)

def up(event):
    global dx, dy
    dx, dy = 0, -1

def down(event):
    global dx, dy
    dx, dy = 0, 1

def left(event):
    global dx, dy
    dx, dy = -1, 0

def right(event):
    global dx, dy
    dx, dy = 1, 0

root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)

draw()
root.after(100, game_loop)
root.mainloop()
    