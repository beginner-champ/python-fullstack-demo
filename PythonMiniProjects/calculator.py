import tkinter as tk

def on_click(btn):
    if btn == "=":
        try:
            result = eval(entry.get())  
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")                                                              
    elif btn == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn)

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry
entry = tk.Entry(root, width=25, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row = 1
col = 0
for btn in buttons:
    action = lambda x=btn: on_click(x)
    btn_widget = tk.Button(root, text=btn, width=5, height=2, command=action)
    btn_widget.grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
