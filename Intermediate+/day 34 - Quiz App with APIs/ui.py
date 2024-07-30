from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#fff"
FONT_TEXT = ("Arial", 18, "italic")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: ", bg=THEME_COLOR, font=("Sans", 15, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.quiz_text = self.canvas.create_text(150, 100, text="sample text", width=280, fill=THEME_COLOR,
                                                 font=FONT_TEXT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, borderwidth=0, command=lambda: self.check_answer("True"))
        self.true_button.grid(column=0, row=2, padx=(20, 0), pady=(20, 0))

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, borderwidth=0, command=lambda: self.check_answer("False"))
        self.false_button.grid(column=1, row=2, padx=(0, 20), pady=(20, 0))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, answer: str):
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(ms=300, func=self.get_next_question)

