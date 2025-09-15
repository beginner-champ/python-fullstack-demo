import tkinter as tk
from tkinter import ttk
root = tk.Tk()
ttk.Label(root, text="Register").pack(pady=10)
ttk.Button(root, text="Click Me").pack()
style = ttk.Style()
style.theme_create("mytheme", parent="alt", settings={
"TButton": {
"configure": {"padding": 10, "background": "#343", "foreground": "cyan"}
},
"TLabel": {
"configure": {"font": ("Arial", 11)}
}
})
style.theme_use("mytheme")
style.theme_use('clam')
style.configure("My.TButton", foreground="blue", background="red", font=("Arial", 12))
ttk.Button(root, text="Styled", style="My.TButton").pack()
print("Registered")
root.mainloop()