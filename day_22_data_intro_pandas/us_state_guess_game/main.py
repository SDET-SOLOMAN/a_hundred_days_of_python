import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title('SDET SOLOMAN\'s US STATES GAME')
image = 'blank_states_img.gif'
screen.addshape(image)

state_text = Turtle()
state_text.shape(image)
state_text.color("red")
state_text.penup()

us_states_file = pandas.read_csv("50_states.csv")
states = us_states_file.state.to_list()

guess_states = []
right_guesses = 0

while len(guess_states) < 50:

    question_answer = screen.textinput(title="Guess the State? ", prompt="Whats the state? ").title()
    print(question_answer)

    if question_answer == 'Exit':
        break

    if question_answer not in guess_states and question_answer in states:
        state_guessed = us_states_file[us_states_file.state == question_answer]
        guess_x = int(state_guessed.x)
        guess_y = int(state_guessed.y)

        state_text.penup()
        state_text.setposition(guess_x, guess_y)
        state_text.write(question_answer)

        guess_states.append(question_answer)

states_to_learn = {

    'states': [x for x in states if x not in guess_states]

}

turtle.mainloop()

datas = pandas.DataFrame(states_to_learn)
datas.to_csv('states_to_learn')