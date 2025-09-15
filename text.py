import tkinter as tk
root=tk.Tk()
label = tk.Label(root,text="Hello World!", font=("arial",14), fg="blue")
label.pack()
text = tk.Text(root,height=5, width=30)
text.pack()
data = text.get("1.0", tk.END)
root.mainloop()