import tkinter
root = tkinter.Tk()

name_label = tkinter.Label(root, text="enter name")
name_label.pack()
name_textbox=tkinter.Entry(root)
name_textbox.pack()

root.mainloop()