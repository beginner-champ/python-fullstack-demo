import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        # Quiz data
        self.questions = [
            {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
            {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris"], "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter"], "answer": "Mars"},
        ]

        self.current_question = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        # Widgets
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(3):  # assuming 3 options per question
            rb = tk.Radiobutton(self.root, text="", variable=self.selected_option,
                                value="", font=("Arial", 12))
            rb.pack(anchor="w")
            self.option_buttons.append(rb)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.prev_btn = tk.Button(self.root, text="Previous", command=self.prev_question)
        self.prev_btn.pack(side="left", padx=20, pady=20)

        self.next_btn = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_btn.pack(side="right", padx=20, pady=20)

        self.load_question()

    def load_question(self):
        self.selected_option.set("")
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=option)

        self.update_navigation_buttons()

    def update_navigation_buttons(self):
        self.prev_btn.config(state="normal" if self.current_question > 0 else "disabled")
        self.next_btn.config(text="Submit" if self.current_question == len(self.questions) - 1 else "Next")

    def next_question(self):
        if not self.selected_option.get():
            self.result_label.config(text="Please select an option.")
            return

        correct_answer = self.questions[self.current_question]["answer"]
        if self.selected_option.get() == correct_answer:
            self.score += 1

        if self.current_question == len(self.questions) - 1:
            self.show_result()
        else:
            self.current_question += 1
            self.load_question()

    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.load_question()

    def show_result(self):
        self.question_label.pack_forget()
        for rb in self.option_buttons:
            rb.pack_forget()
        self.prev_btn.pack_forget()
        self.next_btn.pack_forget()

        self.result_label.config(text=f"Quiz Completed! Your score: {self.score}/{len(self.questions)}")
        self.result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
