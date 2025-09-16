import tkinter as tk
print("Script started")
def login():
 user = username_entry.get()
 pwd = password_entry.get()
 if user == "admin" and pwd =="1234":
  status_label.config(text="login Successfull",fg="green")
 else:
  status_label.config(text="invalid credentials",fg="red")
root=tk.Tk()
root.title("login Form")
window_width = 300
window_height = 200

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

tk.Label(root,text="Username").pack(pady=5)
username_entry=tk.Entry(root)
username_entry.pack()
tk.Label(root,text="Password").pack(pady=5)
password_entry = tk.Entry(root,show="*")
password_entry.pack()
tk.Button(root,text="Login",command=login).pack(pady=10)
status_label = tk.Label(root,text="")
status_label.pack()
root.mainloop()
