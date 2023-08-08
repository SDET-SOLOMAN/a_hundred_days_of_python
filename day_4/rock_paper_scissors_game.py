from random import choice

while True:

    print("Welcome to the Game")
    user_choice = input('Pick: Rock, Paper, or Scissors\n').lower()
    user_score = 0
    computer_score = 0

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    game_choices = {"rock": rock, "paper": paper, "scissors": scissors}

    while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
        user_choice = input('Whats your choice, rock, paper or scissors?').lower()

    while user_score <= 2 and computer_score <= 2:

        user_choice_art = game_choices[user_choice]
        computer_choice = choice(['rock', 'paper', 'scissors'])
        computer_choice_art = game_choices[computer_choice]
        user_wins = f'User win, user picked {user_choice_art} and comp picked {computer_choice_art}'
        comp_wins = f'COMP win, user picked {user_choice_art} and comp picked {computer_choice_art}'

        if user_choice == computer_choice:
            print(f"It's A Draw, user {user_choice_art} and comp {computer_choice_art}")
        elif user_choice == 'rock' and computer_choice == 'scissors':
            user_score += 1
            print(user_wins, f"User score {user_score} vs computer score {computer_score}")
        elif user_choice == 'paper' and computer_choice == 'rock':
            user_score += 1
            print(user_wins, f"User score {user_score} vs computer score {computer_score}")
        elif user_choice == 'scissors' and computer_choice == 'paper':
            user_score += 1
            print(user_wins, f"User score {user_score} vs computer score {computer_score}")
        else:
            computer_score += 1
            print(comp_wins, f"User score {user_score} vs computer score {computer_score}")

        if user_score < 3 and computer_score < 3:
            user_choice = input('Pick Rock, Paper, or Scissors\n').lower()

    if user_score > computer_score:
        print(f"user wins, user's score is {user_score} and computer's score is {computer_score}")
    else:
        print(f"Computer wins, user's score is {user_score} and computer's score is {computer_score}")

    user_answer = input("Do you want to play? y or n").lower()

    if user_answer == 'y':
        print("Welcome to the Game")
        user_choice = input('Pick Rock, Paper, or Scissors\n').lower()
        user_score = 0
        computer_score = 0
    else:
        break