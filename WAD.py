import tkinter as tk
import random
import math

root = tk.Tk()
root.title("Whack-A-Dot")
root.geometry("500x500")

canvas = tk.Canvas(root, bg="white", width=460, height=400)
canvas.pack(padx=10, pady=10)

score = 0
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack(pady=4)

dot_x = 100
dot_y = 100

DOT_R = 25

MOVE_MS = 1000

def draw_dot(x, y):

    return canvas.create_oval(x-DOT_R, y-DOT_R, x+DOT_R, y+DOT_R, fill="red", outline="")

current_dot_id = draw_dot(dot_x, dot_y)

CAN_W = 460
CAN_H = 400

def move_dot():

    global dot_x, dot_y, current_dot_id

    canvas.delete(current_dot_id)

    dot_x = random.randint(DOT_R, CAN_W - DOT_R)

    dot_y = random.randint(DOT_R, CAN_H - DOT_R)

    current_dot_id = draw_dot(dot_x, dot_y)

    root.after(MOVE_MS, move_dot)

root.after(MOVE_MS, move_dot)

def on_click(event):
    global score

    dx = event.x - dot_x

    dy = event.y - dot_y
    
    dist = math.hypot(dx, dy)

    if dist <= DOT_R:

        score += 1

        score_label.config(text=f"Score: {score}")

        move_dot()

canvas.bind("<Button-1>", on_click)

root.mainloop()