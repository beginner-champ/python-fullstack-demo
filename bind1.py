import tkinter as tk
def on_click(event):
 print("Widget clicked at:", event.x, event.y)
root = tk.Tk()
label = tk.Label(root, text="Click me")
label.bind("<Button-1>", on_click)
label.pack()
button = tk.Button(root, text="Click")
button.pack()
button.bind("<Button-1>", on_click)
root.mainloop()