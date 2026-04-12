import tkinter as tk

root = tk.Tk()
root.title("Tkinter calculator")


title = tk.Label(root, text="Simple Calculator", font=("Arial", 18))

tk.Label(root, text="A:").grid(row=1, column=0, sticky="e", padx=5)
entry_a = tk.Entry(root, width=12, justify="right")
entry_a.grid(row=1, column=1,padx=5, pady=5)
title.grid(row=0, column=0, columnspan=4, pady=10)

tk.Label(root, text="B:").grid(row=1, column=2, sticky="e", padx=5)
entry_b = tk.Entry(root, width=12, justify="right")
entry_b.grid(row=1, column=3,padx=5, pady=5)

result_label = tk.Label(root, text="Result:--", font=("Arial", 14))
result_label.grid(row=2, column=0, columnspan=4, pady=8)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=4)

def parse_inputs():
    a_text = entry_a.get().strip()
    b_text = entry_b.get().strip()
    if a_text == "" or b_text =="":
        raise ValueError("Please enter both A and B.")
    a = float(a_text)
    b = float(b_text)
    return a, b

def show_result(value):
    result_label.config(text=f"Result: {value}")
    error_label.config(text="")

def show_error(msg):
    error_label.config(text=msg)
    result_label.config(text="Result: --")

def op_add():
    try:
        a, b = parse_inputs()
        show_result(a + b)
    except ValueError as e:
        show_error(str(e))

def op_sub():
    try:
        a, b = parse_inputs()
        show_result(a - b)
    except ValueError as e:
        show_error(str(e))

def op_mul():
    try:
        a, b = parse_inputs()
        show_result(a * b)
    except ValueError as e:
        show_error(str(e))

def op_div():
    try:
        a, b = parse_inputs()
        if b == 0:
            raise ValueError("Cannot divide by zero. ")
        show_result(a / b)
    except ValueError as e:
        show_error(str(e))

btn_add = tk.Button(root, text="+", width=6, command=op_add)
btn_sub = tk.Button(root, text="-", width=6, command=op_sub)
btn_mul = tk.Button(root, text="×", width=6, command=op_mul)
btn_div = tk.Button(root, text="÷", width=6, command=op_div)

btn_add.grid(row=4, column=0, pady=6)
btn_sub.grid(row=4, column=1)
btn_mul.grid(row=4, column=2)
btn_div.grid(row=4, column=3)


def clear_all():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_label.config(text="Result: --")
    error_label.config(text="")

clear_btn = tk.Button(root, text="Clear", width=8, command=clear_all)
clear_btn.grid(row=5, column=0, columnspan=2, pady=8)

quit_btn = tk.Button(root, text="Quit", width=8, command=root.destroy)
quit_btn.grid(row=5, column=2, columnspan=2)

for c in range(4):
    root.grid_columnconfigure(c, weight=1)

root.mainloop()