from tkinter import *

from day_31_trivia_app_using_api.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = "Sdet Soloman's History Trivia"
        self.window.config(bg=THEME_COLOR, width=400, height=800, pady=20)

        self.score = Label(text=f"Score: {0}", pady=20, padx=20, bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=250, height=250, bg="white", highlightthickness=0)
        self.text_canvas = self.canvas.create_text(
            125, 125, text="text", font=("Arial", 20, 'italic'), fill='black', width=230
        )
        self.canvas.grid(row=1, column=0, pady=40, padx=40, columnspan=2)

        self.cross_image = PhotoImage(file="./images/false.png")
        self.red_button = Button(image=self.cross_image, highlightthickness=0, command=self.red_clicked)
        self.red_button.grid(row=2, column=1)

        self.check_image = PhotoImage(file="./images/true.png")
        self.green_button = Button(image=self.check_image, highlightthickness=0, command=self.green_clicked)
        self.green_button.grid(row=2, column=0)

        self.next_questions()
        self.window.mainloop()

    def red_clicked(self):
        self.answer_check(self.quiz.check_answer("false"))

    def green_clicked(self):
        self.answer_check(self.quiz.check_answer("true"))

    def answer_check(self, user_answer):
        if user_answer:
            self.canvas.config(bg="green")
            self.green_button.config(state='disabled')
            self.green_button.config(state='disabled')
        else:
            self.canvas.config(bg='red')
            self.green_button.config(state='disabled')
            self.green_button.config(state='disabled')
        self.window.after(2000, self.next_questions)

    def next_questions(self):
        self.green_button.config(state='active')
        self.green_button.config(state='active')
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.text_canvas, text=q)
        else:
            self.canvas.itemconfig(self.text_canvas, text="Out of Questions, thanks for playing")
            self.green_button.config(state='disabled')
            self.green_button.config(state='disabled')
