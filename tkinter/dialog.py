from tkinter import filedialog

file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
print("Selected file:",file_path)
save_path = filedialog.asksaveasfilename(defaultextension=".txt")
print("Save as:",save_path)