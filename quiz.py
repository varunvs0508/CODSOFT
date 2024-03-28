import tkinter as tk
from tkinter import messagebox
import random

class QuizApp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("400x300")
        self.questions = questions
        self.score = 0
        self.current_question = None
        self.create_widgets()
        self.show_next_question()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="", wraplength=380)
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(self, text="Score: 0")
        self.score_label.pack()

    def show_next_question(self):
        self.current_question = random.choice(list(self.questions.items()))
        question_text, _ = self.current_question
        self.question_label.config(text=question_text)

    def check_answer(self):
        if self.current_question is None:
            return

        _, correct_answer = self.current_question
        user_answer = self.answer_entry.get().strip()

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Your answer is incorrect. The correct answer is {correct_answer}.")

        self.score_label.config(text=f"Score: {self.score}")
        self.answer_entry.delete(0, tk.END)
        self.show_next_question()

# Quiz questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest mammal?": "Blue whale",
    "What is the boiling point of water in Celsius?": "100"
}

if __name__ == "__main__":
    app = QuizApp(questions)
    app.mainloop()
