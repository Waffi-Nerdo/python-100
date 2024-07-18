# THE HANGMAN GAME

import random

word_list = ["ifeoluwa", "adetara", "jumia"]

lives = 6



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# todo 1 - Randomly choose a word from the word_list
chosen_word = random.choice(word_list)


#Testing the code
print(f'the chosen word is {chosen_word}')

end_of_game = False

display = []
for letter in chosen_word:
    display.append("_") 

while not end_of_game:
    # todo2 - ask the user to guess a letter and assign it to the variable guess
    guess = input("Hi User guess a letter: ").lower()

    # todo 3 - check if the letter the user guessed (guess is in the chosen word)
    if guess in display:
        print("you have already guessed that letter")
    for letter in chosen_word:
        if letter == guess:
            print("Right")
        else:
            print("Wrong")


    # todo 4 - create an empty list called display
    # for each letter in the chosen_word, add a "_" to 'display'


    

    # solution below is correct they both work the same
    # for _ in range(len(chosen_word)):
    #     display += "_"

    # print(display)


    #todo 5 loop through each position in the chosen_word
    #if the letter at that position mateches "guess" then reveal that letter in the display at that position

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        print(f"you guessed {guess} thats not in the word you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])
