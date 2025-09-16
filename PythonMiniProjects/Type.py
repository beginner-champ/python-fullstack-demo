import tkinter as tk
import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing speed is measured in words per minute.",
    "Practice makes perfect when typing fast.",
]

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("600x300")

        self.sentence = random.choice(sentences)
        self.start_time = None

        self.sentence_label = tk.Label(root, text=self.sentence, font=("Arial", 14), wraplength=500)
        self.sentence_label.pack(pady=20)

        self.text_entry = tk.Entry(root, font=("Arial", 14), width=60)
        self.text_entry.pack()
        self.text_entry.bind("<FocusIn>", self.start_timer)
        self.text_entry.bind("<Return>", self.check_result)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.reset_button = tk.Button(root, text="Try Another", command=self.reset)
        self.reset_button.pack(pady=10)

    def start_timer(self, event):
        if not self.start_time:
            self.start_time = time.time()

    def check_result(self, event):
        end_time = time.time()
        typed_text = self.text_entry.get()
        elapsed = end_time - self.start_time
        words = len(typed_text.split())
        wpm = round((words / elapsed) * 60)
        accuracy = self.calculate_accuracy(typed_text)

        self.result_label.config(
            text=f"Time: {round(elapsed, 2)} sec | WPM: {wpm} | Accuracy: {accuracy}%"
        )

    def calculate_accuracy(self, typed):
        correct_chars = sum(1 for a, b in zip(typed, self.sentence) if a == b)
        total_chars = len(self.sentence)
        return round((correct_chars / total_chars) * 100)

    def reset(self):
        self.sentence = random.choice(sentences)
        self.sentence_label.config(text=self.sentence)
        self.text_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None


# Run App
root = tk.Tk()
app = TypingSpeedTester(root)
root.mainloop()

