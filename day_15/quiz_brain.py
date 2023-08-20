class QuizBrain:

    def __init__(self, question_answer):
        self.number = 0
        self.question_list = question_answer
        self.questions_left = len(self.question_list) - 1
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.number]
        self.number += 1
        print(f"Question number: {self.number}:\n"
              f"Question's topic: {current_question.category}\n"
              f"Question's difficulty is {current_question.difficulty}\n"
              f"Question: {current_question.text}")
        user_input = input("True or False? ").lower()
        self.check_answer(current_question.answer.lower(), user_input)

    def still_has_questions(self):
        while self.questions_left >= self.number:
            print(f"Your current score is: {self.score}")
            self.next_question()

    def check_answer(self, right_answer, user_answer):
        if user_answer == right_answer:
            self.score += 1
            print("Correct!")
        else:
            print(f"Sorry, wrong, the correct answer is: {right_answer}")
