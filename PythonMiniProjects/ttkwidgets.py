import tkinter as tk
from tkinter import ttk
root = tk.Tk()
ttk.Label(root, text="Register").pack(pady=10)
ttk.Button(root, text="Click Me").pack()
print("Registered")
root.mainloop()