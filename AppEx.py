import tkinter as tk

class MyApp:
 def __init__(self, root):
  self.root = root
  self.root.title("OOP Tkinter Example")
  self.label = tk.Label(root, text="Hello, Tkinter with Classes!")
  self.label.pack(pady=20)
  self.button = tk.Button(root, text="Click Me", command=self.on_click)
  self.button.pack()
 def on_click(self):
  self.label.config(text="Button Clicked!")
if __name__ == "__main__":
 root = tk.Tk()
 app = MyApp(root)
 root.mainloop()