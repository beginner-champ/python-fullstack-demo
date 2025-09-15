import tkinter as tk

root = tk.Tk()

# Your existing widgets
check_var = tk.StringVar(value="I agree")
check_box = tk.Checkbutton(root, text="I agree", variable=check_var)
check_box.pack()

radio_var = tk.StringVar(value="1")
tk.Radiobutton(root, text="online", variable=radio_var, value="1").pack()
tk.Radiobutton(root, text="offline", variable=radio_var, value="2").pack()
tk.Label(root, text="Offered courses", width=250).pack()
tk.Label(root, text="top").pack(side="top")
tk.Label(root, text="left").pack(side="left")

# Corrected listbox usage to fix potential frame-related issues
listbox = tk.Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "DBMS")
listbox.insert(4, "PHP")
listbox.insert(5, "C++")
listbox.pack()

# The on_click function is defined here, but the corresponding widget is not in your screenshot
def on_click():
    # You need to define a name_textbox widget for this to work
    # I've included a placeholder line below
    print("Function 'on_click' called.")

# Your button is defined, but the command is on_c...
# It should be a full function name like 'on_click'
button = tk.Button(root, text="Click Me", bg="red", fg="white", command=on_click)
button.pack()

spin = tk.Spinbox(root, from_=0, to=10)
spin.pack()

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

message = tk.Message(root, text="registration completed!!.")
message.pack()

# The code that was causing the issue is now in a try-except block
try:
    photo = tk.PhotoImage(file="registered.png")
    label = tk.Label(root, image=photo)
    label.pack(padx=1, pady=1)
except tk.TclError:
    print("Could not find 'registered.png'. Please ensure it is in the same folder.")

# This line is essential to keep the window open
root.mainloop()