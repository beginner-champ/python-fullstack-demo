import tkinter as tk
import tkinter.ttk as ttk
root=tk.Tk()
notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")
tk.Label(tab1, text="This is Tab 1").pack()
tk.Label(tab2, text="This is Tab 2").pack()
root.mainloop()