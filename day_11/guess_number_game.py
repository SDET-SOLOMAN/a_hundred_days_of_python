from arts.day_11_art import logo
from random import randint

SUPER_EASY = 15
EASY = 10
HARD = 5
SUPER_HARD = 3
COMP_CHOICE = randint(1, 100)

print(logo)
print(COMP_CHOICE)


def user_choice():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    user = input("Choose a difficulty. Type: 'super easy', 'easy', 'hard' or super hard: \n").lower()

    if user == 'easy':
        return EASY
    elif user == 'super easy':
        return SUPER_EASY
    elif user == 'hard':
        return HARD
    return SUPER_HARD


def game(number):
    user_guess = None

    while COMP_CHOICE != user_guess and number > 0:

        print(f"You have {number} attempts remaining to guess the number.")
        user_guess = int(input('Make a guess: '))

        if user_guess < COMP_CHOICE:
            print('Too Low')
            number -= 1
        elif user_guess > COMP_CHOICE:
            print("Too High")
        else:
            print(f"congrats you have won, comp choice was {COMP_CHOICE} and ur guess was {user_guess}")
            break

    if number == 0:
        print("You have no attempts left, You Lose")


game(user_choice())
# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
