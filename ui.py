from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="test",
            width=280,
            font=("Arial", 14, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: ", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, bd=0, command=self.true_button_press)
        self.false_button = Button(image=false_img, highlightthickness=0, bd=0, command=self.false_button_press)

        self.true_button.grid(column=1, row=2)
        self.false_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="yellow")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
