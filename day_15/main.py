from question_model import Quiz
from arts.day_15 import question_data
from quiz_brain import QuizBrain

question_bank = []

for char in question_data:
    question = char['question']
    answer = char['correct_answer']
    topic = char['category']
    diff = char['difficulty']
    question_bank.append(Quiz(question, answer, topic, diff))

quiz = QuizBrain(question_bank)
quiz.still_has_questions()

print(f"Congrats, you have completed my SDET SOLOMAN Quiz,\n"
      f"total correct answers: {quiz.score} out of {quiz.number} questions")