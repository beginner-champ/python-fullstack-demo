import tkinter as tk
from tkinter import ttk, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish To-Do List")
        self.root.geometry("500x400")


        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))

        
        self.task_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.task_var, width=40).pack(pady=10)

        
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=5)
        ttk.Button(btn_frame, text="Add Task", command=self.add_task).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Remove Selected", command=self.remove_task).pack(side="left", padx=5)

        
        self.tree = ttk.Treeview(root, columns=("Task",), show="headings", selectmode="browse")
        self.tree.heading("Task", text="Task")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tree.insert("", "end", values=(task,))
            self.task_var.set("")
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected)
        else:
            messagebox.showwarning("No Selection", "Select a task to remove.")


root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
