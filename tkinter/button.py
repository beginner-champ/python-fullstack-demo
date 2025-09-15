import tkinter as tk
root=tk.Tk()
def on_click():
    print("Button clicked!")
    button = tk.Button(root, text="Click Me", command=on_click)
    button.pack()
root.mainloop()