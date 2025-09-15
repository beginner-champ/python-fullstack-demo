import tkinter as tk
root = tk.Tk()
label = tk.Label(root,text="Welcome", font=("Times New Roman",14), fg="navyblue")
label.pack()

name_label = tk.Label(root, text="Enter Name:",fg="navyblue")
name_label.pack()
name_textbox=tk.Entry(root,width=150)
name_textbox.pack()

name_label = tk.Label(root, text="Qualification:",fg="navyblue")
name_label.pack()
name_textbox=tk.Entry(root,width=150)
name_textbox.pack()


def on_click() :
    print(f"name entered:{name_textbox.get()}")
    print(f"Checkbox value:{check_var.get()}")
    print(f"Radiobutton value: {radio_var.get()}")
    selected_items = listbox.get(listbox.curselection())
    for index in selected_items:
        print(f"Selected course:{listbox.get(index)}")

frame = tk.Frame(root,bg="#5C9CAB",width=250)
frame.pack(padx=5,pady=2)
tk.Label(frame,text="Hello",bg="Navyblue", fg="white").pack()
check_var = tk.IntVar()
check = tk.Checkbutton(root,text="I agree", variable=check_var)
check.pack()

radio_var=tk.StringVar(value="1")

tk.Radiobutton(root,text="online", variable=radio_var,value="1").pack()
tk.Radiobutton(root,text="offline", variable=radio_var,value="2").pack()
tk.Label(frame,text="Offered Courses",width=250).pack()
tk.Label(root, text="Top").pack(side="top")
tk.Label(root, text="Left").pack(side="left")
frame.pack(padx=15,pady=5)
listbox =tk.Listbox(frame)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "DBMS")
listbox.insert(4, "PHP")
listbox.insert(5, "C++")
listbox.pack()

button = tk.Button(root, text="Click Me",bg="red",fg="white", command=on_click)
button.pack()

spin = tk.Spinbox(root,from_=0,to=10)
spin.pack()

scale=tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

message = tk.Message(root, text="registration completed!!.")
message.pack()

photo = tk.PhotoImage(file="registered.png")
label = tk.Label(root, image=photo)
label.pack(padx=1,pady=1)
label.pack()

root.mainloop()