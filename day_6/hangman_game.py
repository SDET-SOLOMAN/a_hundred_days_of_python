import random
from arts.day_6_art import word_list, logo, stages

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create game blanks
display = ["_" for x in chosen_word]
guessed_letters = ""

# Actual Game
while not end_of_game:

    guess = input("Guess a letter:\n").lower()

    while guess in guessed_letters:

        print(f"This letter: {guess} was already guessed \n"
              f"Plz try another one")

        guess = input("Guess a letter:\n").lower()

    guessed_letters += guess

    # Check guessed letter
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        # If the letter is not in the chosen_word, prints out the letter and lets them know it's not in the word.
        lives -= 1
        # Decreasing lives
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    # Checks if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])