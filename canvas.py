import tkinter as tk
root=tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.create_line(10, 10, 50, 50, fill="red", width=3)

canvas.create_rectangle(50, 50, 100, 100, outline="blue", fill="lightblue")

canvas.create_oval(60, 60, 80, 80, fill="green")

scrollbar = tk.Scrollbar(root)
text = tk.Text(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
text.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

paned = tk.PanedWindow(root, orient="horizontal")
paned.pack(fill="both", expand=True)
left = tk.Label(paned, text="Accept", bg="Green")
right = tk.Label(paned, text="Deny", bg="Red")
paned.add(left)
paned.add(right)

def open_window():
 win = tk.Toplevel(root)
 win.title("New Window")
 tk.Label(win, text="I'm a new window!").pack()
 tk.Button(root, text="Open Window", command=open_window).pack()

 
root.mainloop()