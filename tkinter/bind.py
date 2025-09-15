
import tkinter as tk

def greet():
 print("Hello!")
root = tk.Tk()

button = tk.Button(root, text="Click", command=greet)
button.pack()
root.mainloop()
