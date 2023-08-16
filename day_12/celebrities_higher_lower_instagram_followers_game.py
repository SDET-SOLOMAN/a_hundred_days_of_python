from arts.day_12 import logo, data, vs
from random import choice

SCORE = 0


def celebrity():
    celebrity1, celebrity2 = choice(data), choice(data)
    while celebrity1 == celebrity2:
        choice(data)
    return [celebrity1, celebrity2]


def follower_checker(a, b):
    if a > b:
        return 'a'
    return 'b'


def game():
    global SCORE
    print(logo)

    if SCORE > 0:
        print(f"You're right! Current score: {SCORE}.")
    A, B = celebrity()

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_answer == follower_checker(A['follower_count'], B["follower_count"]):
        SCORE += 1
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        SCORE = 0

    if SCORE > 0:
        game()


game()
