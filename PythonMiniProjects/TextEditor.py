import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser


def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        try:
            with open(path, "r") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file:\n{e}")


def save_file():
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if path:
        try:
            with open(path, "w") as file:
                content = text_area.get("1.0", tk.END)
                file.write(content)
            messagebox.showinfo("Saved", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")


def clear_text():
    confirm = messagebox.askyesno("Clear Text", "Are you sure?")
    if confirm:
        text_area.delete("1.0", tk.END)


def change_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(fg=color)


# Main Window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

# Text Area
text_area = tk.Text(root, font=("Arial", 14))
text_area.pack(expand=True, fill='both')

# Menu Bar
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
